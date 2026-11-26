# Independent mathematical audit

## correctness

PASS

The journal PDF confirms the exact ODE in Eq. (2.1), the printed denominator μ(B+μ) in Eq. (2.4), the no-positive-equilibrium assertion immediately following it, and the global stability assertion in Theorem 4.1. The I row of the full Jacobian at (B/η,0,0) has only the diagonal entry MB/η−(μ+η), giving the threshold in the Finding. For the full perturbation the remainder includes a mixed I(S−B/η) term; the proof's O(I²) notation is valid along S=B/η and does not affect the Jacobian argument. Summing the equations gives N'=B−ηN. At an endemic equilibrium R=μI/(α+η) and S=(μ+η)/[M(1+γI)], so N=B/η gives exactly the reported quadratic. For 0<ℛ<1 its leading and constant terms are positive. Positivity of the root sum and discriminant require z=Bγ/k>1 and (z−1)²>4z(1−ℛ)/ℛ; the upper discriminant root gives the strict reported bound (equality gives one double root). S and R are positive upon back-substitution. At the witness both thresholds are 1/2. In coordinates (N,I,R) the independently checked characteristic factors are (x+1)²(x+2), (x+1)(36x²+43x−42)/36, and (x+1)(5x²+12x+14)/5: respectively all negative eigenvalues, opposite-sign quadratic roots, and a conjugate pair with negative real part. The two attracting equilibria are local statements; even the constant trajectory at either positive equilibrium refutes global attraction. Replay: `python3 /workspace/branches/independent-checks.py 3` (SymPy exact substitutions); the uploaded checker was read, not run. No general basin or phase portrait follows.

## originality

PASS

This is a source-specific correction of the printed positive-parameter ODE, not a claim to discover backward bistability or discriminant methods. The cited article has the model but gives conflicting threshold and equilibrium conclusions. The inspected related records have different state equations. No examined result supplies the corrected threshold and sharp root criterion together with this exact stable–saddle–stable witness for the printed system.

## value

PASS

It corrects a consequential qualitative claim in a published ODE and separates the bad invasion formula from genuine subthreshold bistability. The all-positive exact witness with both thresholds equal eliminates a natural alternative explanation of the contradiction. The sharp multiplicity condition gives more than an isolated example; the result is mathematical and does not assert a real-world transmission conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
