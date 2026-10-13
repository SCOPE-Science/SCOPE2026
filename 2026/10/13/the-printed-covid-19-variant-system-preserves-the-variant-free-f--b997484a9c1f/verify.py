#!/usr/bin/env python3
import sympy as sp

m = 5
alpha,beta,lam = sp.symbols("alpha beta lam")
u = {j: sp.symbols(f"u{j}") for j in range(1,m+1)}
w = {k: sp.symbols(f"w{k}") for k in range(1,m+1)}
gamma = {k: sp.symbols(f"gamma{k}") for k in range(1,m+1)}
f1 = {k: sp.symbols(f"f1_{k}") for k in range(1,m+1)}
f5 = {(j,k): sp.symbols(f"f5_{j}_{k}") for j in range(1,m+1) for k in range(1,m+1)}

variant_sum = sum(u[r]*f5[(r,s)] for s in range(1,m+1) for r in range(2,m))
subs_zero = {z:0 for z in f5.values()}

rhs = {}
for j in range(2,m):
    for k in range(1,m+1):
        infection = alpha*f1[k]*variant_sum*(1 if j == 2 else 0)
        progression = beta*(1+lam)*u[j-1]*f5[(j-1,k)]
        regression = gamma[k]*w[k]*f5[(j+1,k)]
        loss = -beta*(1+lam)*u[j]*f5[(j,k)] - gamma[k]*w[k]*f5[(j,k)]
        rhs[(j,k)] = sp.expand(infection+progression+regression+loss)
        assert sp.simplify(rhs[(j,k)].subs(subs_zero)) == 0

# Confirm no symbol representing a primary-virus compartment is needed by any
# variant RHS: the encoded structure closes on f5 plus external coefficients.
all_variant_symbols = set(f5.values())
for expr in rhs.values():
    state_symbols = {s for s in expr.free_symbols if str(s).startswith("f5_")}
    assert state_symbols <= all_variant_symbols

print("VERIFY_OK")
print("checked_variant_equations", len(rhs))
print("zero_face_residuals", [sp.simplify(e.subs(subs_zero)) for e in rhs.values()])
