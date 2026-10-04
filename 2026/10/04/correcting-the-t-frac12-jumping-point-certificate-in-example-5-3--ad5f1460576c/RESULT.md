# Correcting the \(t=\frac12\) jumping-point certificate in Example 5.3

## Finding

Consider the reduced line arrangement
\[
C_t: xyz(x-z)(x-2z)(x-tz)(y-z)(y-2z)(y-(t+1)z)(x-y)(x-y+z)=0
\]
in \(\mathbb P^2_{\mathbb C}\). Example 5.3 of Marchesi--Vallès prints, for \(t=\frac12\), the relation matrix
\[
\begin{bmatrix}-7x+11y-7z\\14x-134y+161z\\4y^2-7yz\end{bmatrix}
\]
and the jumping point \([17:21:16]\). Exact recomputation shows that these coefficients do not belong to the \(t=\frac12\) member.

For \(t=\frac12\), after rescaling and reordering the minimal Jacobian syzygy generators, a valid minimal relation matrix is
\[
A_{1/2}=\begin{bmatrix}-3x+5y-3z\\3x-29y+30z\\2y^2-3yz\end{bmatrix}.
\]
The two linear entries meet at
\[
P_{1/2}=[7:9:8].
\]
All eleven line factors of \(C_{1/2}\) are nonzero at this point, so \(P_{1/2}\notin C_{1/2}\). Thus the qualitative conclusion of the example, that the jumping point is outside the arrangement for this parameter, remains correct.

The same exact computation at \(t=\frac23\) reproduces the published matrix, up to the same harmless generator normalizations,
\[
\begin{bmatrix}-5x+8y-5z\\15x-144y+165z\\6y^2-10yz\end{bmatrix},
\]
with jumping point \([4:5:4]\), which lies on \(C_{2/3}\). At \(t=\frac34\), the computation gives
\[
\begin{bmatrix}-7x+11y-7z\\14x-134y+161z\\4y^2-7yz\end{bmatrix},
\]
with jumping point \([17:21:16]\). This is exactly the numerical certificate printed in the source under \(t=\frac12\).

## Assumptions and scope

The ground field is \(\mathbb C\). The claim concerns only the three explicit parameters \(t=\frac12\), \(t=\frac23\), and \(t=\frac34\), and uses the source's definition of the jumping point from the two linear entries of the minimal relation matrix for a nearly free arrangement. No formula for arbitrary \(t\) is claimed, and no part of the general theory of nearly free bundles in the source is challenged.

## Proof

Let \(F_t\) denote a scalar multiple of the defining degree-eleven polynomial chosen so that all coefficients are integral. Write \(AR(F_t)_d\) for the degree-\(d\) Jacobian syzygies. For each of the three parameters, exact coefficient linear algebra produces one primitive generator \(s_0\) in degree \(5\), two new primitive generators \(s_1,s_2\) in degree \(6\), and a unique degree-seven relation after adjoining the three linear multiples of \(s_0\).

For \(t=\frac12\), the primitive relation is
\[
(3yz-2y^2)s_0+(3x-29y+30z)s_1+(3x-5y+3z)s_2=0.
\]
Changing the signs of \(s_0\) and \(s_2\), and ordering the two degree-six generators first, gives the displayed column \(A_{1/2}\). Solving its two linear equations gives \([7:9:8]\). Direct substitution into the eleven line factors gives the nonzero values
\[
7,\ 9,\ 8,\ -1,\ -9,\ 6,\ 1,\ -7,\ -6,\ -2,\ 6,
\]
so the point is outside \(C_{1/2}\).

The same calculation for \(t=\frac23\) yields, in a primitive normalization,
\[
(10yz-6y^2)s_0+(15x-144y+165z)s_1+(5x-8y+5z)s_2=0,
\]
which is equivalent to the source's printed \(t=\frac23\) matrix and gives \([4:5:4]\). For \(t=\frac34\) it yields
\[
(7yz-4y^2)s_0+(14x-134y+161z)s_1+(7x-11y+7z)s_2=0.
\]
After the same sign convention this is exactly the matrix that the source prints under \(t=\frac12\), and its linear entries meet at \([17:21:16]\).

To certify minimality rather than merely exhibit relations, the checker constructs the full Jacobian-syzygy coefficient matrices. Reduction modulo the prime \(1000003\) has ranks \(62\), \(79\), and \(97\) in degrees \(5\), \(6\), and \(7\), respectively. The displayed exact syzygies give matching rational upper bounds on these ranks, so over \(\mathbb Q\) the syzygy dimensions are exactly \(1\), \(5\), and \(11\). Hence the degree-five generator is unique up to scale, there are exactly two new degree-six generators, and the displayed degree-seven relation is unique up to the allowed generator changes.

## Verification

Run `python3 artifacts/verify.py`. The script uses only the Python standard library. It reconstructs the three arrangements from their eleven linear factors, differentiates them exactly, verifies the three primitive Jacobian syzygies for each parameter, verifies the degree-seven relation, computes the modular ranks giving syzygy dimensions \(1,5,11\), checks the three jumping points, and checks whether each point lies on its arrangement. Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Marchesi--Vallès prove the structural theory of nearly free bundles and use Example 5.3 to show that two arrangements with the same combinatorics can place the jumping point inside or outside the arrangement. The source explicitly prints the \(t=\frac12\) and \(t=\frac23\) numerical matrices and points. The current calculation preserves their qualitative conclusion but corrects the first numerical certificate. Exact-phrase and parameter searches located the same printed data in the arXiv text and in an open repository copy of the published article, and did not locate a published erratum or a prior correction of this coefficient-level mismatch.

## Limitations

This result is a correction of one explicit numerical certificate. It does not assert a closed formula for the jumping point for all parameters, classify the realization space of the arrangement combinatorics, or alter the source's general theorems. Literature searches cannot exclude an obscure correction not indexed by the sources checked; that residual bibliographic risk is recorded in the audit.

## References

1. S. Marchesi and J. Vallès, *Nearly free curves and arrangements: a vector bundle point of view*, arXiv:1712.04867, first public 2017-12-13; Math. Proc. Cambridge Philos. Soc. 170 (2021), 51--74, DOI:10.1017/S0305004119000318.
2. The open repository copy of the published article reproduces Example 5.3 with the same \(t=\frac12\) matrix and point as the arXiv version.
