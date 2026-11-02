"""Exact transfer-matrix identity for fan-graph avalanche generating functions.

Run: python checks/transfer_identity.py
Requires SymPy. The arithmetic is over Q(z,t), not floating point.
"""
import sympy as sp

z, t = sp.symbols('z t')
state = [('B', q, s) for q in (0, 1) for s in (0, 1)]
state += [('I', q, None) for q in (0, 1)]
state += [('A', q, None) for q in (0, 1)]
index = {v: k for k, v in enumerate(state)}

def matrix(endpoint):
    result = sp.zeros(8)
    for i, (phase, seen_zero, previous_saturated) in enumerate(state):
        for height in ((0, 1) if endpoint else (0, 1, 2)):
            if height == 0 and seen_zero:
                continue
            q = 1 if height == 0 else 0 if height == 2 else seen_zero
            saturated = (height == 1) if endpoint else (height == 2)
            if phase == 'B':
                result[i, index[('B', q, int(saturated))]] += 1
                if saturated and not previous_saturated:
                    result[i, index[('I', q, None)]] += t
            elif phase == 'I':
                if saturated:
                    result[i, index[('I', q, None)]] += t
                else:
                    result[i, index[('A', q, None)]] += 1
            else:
                result[i, index[('A', q, None)]] += 1
    return result

E = matrix(True)
T = matrix(False)
initial = sp.zeros(1, 8)
initial[0, index[('B', 0, 0)]] = 1
terminal = sp.Matrix([int(s[0] != 'B') for s in state])
# Exactly one full maximal saturated run is marked with weight t per vertex.
marked = sp.factor((z**2 * initial * E * (sp.eye(8)-z*T).inv() * E * terminal)[0])
delta = 1 - 3*z + z**2
B = (2 - 5*z + 2*z**2) / delta**2
expected = z**2*t*(t+B)/(1-t*z)
assert sp.cancel(marked - expected) == 0

# Each of the length-L vertices in a chosen saturated run triggers that run.
nonzero = sp.factor(t*sp.diff(marked, t))
expected_nonzero = z**2*t*B/(1-t*z)**2 + (t*z)**2*(2-t*z)/(1-t*z)**2
assert sp.cancel(nonzero-expected_nonzero) == 0

# Recurrence follows from segments containing at most one zero between 2s.
plain_segment = 1/(1-z)**2
nonempty_segment = plain_segment-1
recurrent = sp.factor(plain_segment-1-2*z + z*nonempty_segment**2/(1-z*plain_segment))
assert sp.cancel(recurrent-z**2*(3-z)/delta)==0

avalanche = sp.factor(z*sp.diff(recurrent,z)-nonzero.subs(t,1)+nonzero)
expected_avalanche = (2*z**2*(1-z)/delta**2
    + t*z**2*B/(1-t*z)**2 + (t*z)**2*(2-t*z)/(1-t*z)**2)
assert sp.cancel(avalanche - expected_avalanche) == 0
assert sp.cancel(avalanche.subs(t,1)-z*sp.diff(recurrent,z)) == 0
print('EXACT_TRANSFER_MATRIX_IDENTITY_PASS')
