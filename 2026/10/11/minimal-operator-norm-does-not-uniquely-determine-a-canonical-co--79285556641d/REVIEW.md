# Review

## Correctness
PASS. The original three-vector family is Parseval, and for every real \(c\),
\[
T_\Lambda V_c=K.
\]
The exact Gram matrix
\[
V_c^*V_c=
\begin{pmatrix}
1&0\\
0&1/4+c^2
\end{pmatrix}
\]
shows that every
\[
|c|\le\frac{\sqrt3}{2}
\]
has norm \(1\). Since
\[
\|K\|=\|T_\Lambda\|=1,
\]
no dual analysis operator can have smaller norm.

## Originality
PASS. Exact-source, minimum-norm, Douglas-reduced-solution, synthesis-kernel, and inherited canonical-\(K\)-dual formulations were searched and compared. Earlier papers repeat the uniqueness convention but do not supply this counterexample or the repaired statement.

The closest indexed dual-frame and \(K\)-frame results optimize different quantities or address range compression. They do not imply the continuum of equal-norm minimizers here.

## Value
PASS. Proposition 3.7 uses uniqueness of the minimum-norm dual to define the canonical controlled \(K\)-\(g\)-dual. The failure persists with identity controls, an invertible \(K\), and a Parseval input frame. The repaired statement cleanly separates operator-norm minimization from the genuinely unique Douglas reduced solution.

## Limitations
The result corrects the uniqueness clause, not existence of a minimum-norm dual. It does not assess stricter pointwise coefficient-minimization criteria. An unindexed correction remains possible.

Same-model review: passed. Independent audit: not yet performed.
