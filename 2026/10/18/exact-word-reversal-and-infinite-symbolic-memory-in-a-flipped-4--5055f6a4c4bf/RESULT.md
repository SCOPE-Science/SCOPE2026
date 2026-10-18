# Exact word reversal and infinite symbolic memory in a flipped \(4\)-expansion

## Finding

The invariant binary digit process of a specific two-branch flipped continued-fraction transformation is **reversible in every finite dimension**, although it is neither independent nor Markov of any finite order.

Let \(F:[1,2]\to[1,2]\) have branches
\[
F(x)=\begin{cases}
5-4/x,&1\le x\le4/3,\\
4/x-1,&4/3<x\le2.
\end{cases}
\]
Initialize \(X_0\) with the invariant probability
\[
d\mu(x)=\frac1{\log3}\left(\frac1x+\frac1{4-x}\right)dx,
\]
and let \(X_{n+1}=F(X_n)\). Label an iterate by \(D_n=0\) on \([1,4/3]\) and by \(D_n=1\) on \((4/3,2]\). For every \(k\ge1\) and every binary word \(w=(d_0,\ldots,d_{k-1})\), write \(w^{\mathrm{rev}}=(d_{k-1},\ldots,d_0)\). Then
\[
\boxed{\Pr(D_0\cdots D_{k-1}=w)=\Pr(D_0\cdots D_{k-1}=w^{\mathrm{rev}}).}
\]

There is also an explicit exact formula for every such probability. Set
\[
Q=\begin{pmatrix}1&1\\1&3\end{pmatrix},\qquad
M_0=\begin{pmatrix}1&1\\0&4\end{pmatrix},\qquad
M_1=\begin{pmatrix}1&1\\4&0\end{pmatrix}.
\]
Form \(K_w=M_{d_0}\cdots M_{d_{k-1}}Q=\begin{pmatrix}a&b\\c&d\end{pmatrix}\). All four entries are positive integers and
\[
\boxed{\Pr(w)=\frac1{\log3}\left|\log\frac{ad}{bc}\right|.}
\]
This is a complete finite-word law, not merely a statement about one- or two-digit marginals.

For each \(n\ge1\), the all-zero cylinder has probability
\[
\boxed{\Pr(0^n)=\frac{\log(1+2\cdot4^{-n})}{\log3}.}
\]
Consequently, the one-sided stationary digit process is **not a Markov chain of any finite order**. In particular, it is not independent: \(\Pr(00)=\log(9/8)/\log3\) whereas \(\Pr(0)=\log(3/2)/\log3\), and these do not satisfy \(\Pr(00)=\Pr(0)^2\).

## Assumptions and scope

All statements concern the specified map \(F\), the displayed absolutely continuous invariant probability, and its stationary itinerary under the two natural branches. Values on the countable union of iterated branch boundaries may be assigned either label: that union has \(\mu\)-measure zero and cannot change any finite-word probability. Logs are natural logarithms. Reversibility is the equality of probabilities of each finite block and its reverse; it is **not** invertibility of the original interval map. The assertion of infinite Markov order is relative to this two-symbol observable, not to arbitrary codings.

The map and its invariant density are from Kraaikamp–Langeveld (2016), Section 2.1. The probabilistic block reversal, explicit all-word formula, and infinite-memory consequence are the present results.

## Proof

**Step 1: conjugacy and invariance.** Set \(z=x/(4-x)\); it sends \([1,2]\) monotonically onto \(J=[1/3,1]\), and the branch boundary \(4/3\) to \(1/2\). The pushforward of \(\mu\) is \(d\nu(z)=dz/(z\log3)\). The two inverse branches of the conjugate interval map \(S\) are
\[
g_0(z)=\frac{1+z}{4}\quad\text{and}\quad
g_1(z)=\frac{1+z}{4z}.
\]
Their images are respectively \([1/3,1/2]\) and \([1/2,1]\), and each is a bijection from \(J\) to the indicated branch interval, up to endpoints. The transfer identity for \(\rho(z)=1/(z\log3)\) follows pointwise:
\[
\frac{\rho(g_0(z))}{4}+\frac{\rho(g_1(z))}{4z^2}
=\frac1{(1+z)\log3}+\frac1{z(1+z)\log3}
=\rho(z).
\]
Moreover \(\int_{1/3}^1 dz/(z\log3)=1\); thus \(\nu\), and therefore \(\mu\), are invariant. This independently checks the density used from the source.

**Step 2: exact cylinders.** The maps \(g_0,g_1\) have Möbius representatives \(M_0,M_1\) from the Finding. Under the standard convention that \(\begin{pmatrix}a&b\\c&d\end{pmatrix}\) acts by \(z\mapsto(az+b)/(cz+d)\), matrix products represent compositions from left to right. Because each branch is onto \(J\), the cylinder specified by \(w\) is the interval \(g_{d_0}\circ\cdots\circ g_{d_{k-1}}(J)\), apart from null boundaries. The columns of \(Q\) represent the endpoints \(1\) and \(1/3\), respectively. Hence if \(K_w=\begin{pmatrix}a&b\\c&d\end{pmatrix}\), the cylinder endpoints are \(a/c\) and \(b/d\). The entries are strictly positive for nonempty words, and integration against \(dz/(z\log3)\) gives precisely
\[
\nu(g_w(J))=\frac{|\log((a/c)/(b/d))|}{\log3}
=\frac{|\log(ad/bc)|}{\log3}.
\]
The determinant of the product is nonzero, so this probability is positive.

**Step 3: exact reversal.** Both branch matrices satisfy
\[
M_0Q=\begin{pmatrix}2&4\\4&12\end{pmatrix},\qquad
M_1Q=\begin{pmatrix}2&4\\4&4\end{pmatrix},
\]
which are symmetric. Equivalently, \(M_jQ=QM_j^{\mathsf T}\) for each \(j\in\{0,1\}\). Iterating this algebraic identity yields
\[
\boxed{M_{d_{k-1}}\cdots M_{d_0}Q=(M_{d_0}\cdots M_{d_{k-1}}Q)^{\mathsf T}.}
\]
Transposition preserves the entries on the diagonal and exchanges off-diagonal entries, thus preserves \(ad/(bc)\). The exact-cylinder formula proves the claimed word-reversal invariance for every length and every word. Invariance from Step 1 makes these finite-block equalities a statement about a stationary process.

**Step 4: infinite memory.** The affine inverse branch \(g_0(z)=1/3+(z-1/3)/4\) fixes \(1/3\), and
\[
g_0^n(J)=\left[\frac13,\frac13+\frac{2}{3\cdot4^n}\right].
\]
Its \(\nu\)-measure is \(\log(1+2\cdot4^{-n})/\log3\). Thus the probability that the next digit is zero given \(n\) consecutive initial zeros is
\[
c_n=\frac{\log(1+2\cdot4^{-(n+1)})}{\log(1+2\cdot4^{-n})}.
\]
For \(0<t\) define \(R(t)=\log(1+t/4)/\log(1+t)\). Direct differentiation shows its derivative has the sign of
\[
H(t)=\tfrac14(1+t)\log(1+t)-(1+t/4)\log(1+t/4).
\]
Here \(H(0)=0\) and \(H'(t)=\tfrac14\log((1+t)/(1+t/4))>0\) for \(t>0\). Thus \(R\) is strictly increasing, so \(c_n=R(2\cdot4^{-n})\) is strictly decreasing. It tends to \(1/4\). If the stationary digit sequence had any finite Markov order \(m\), all conditional probabilities \(c_n\) for \(n\ge m\) would be equal, as their most recent \(m\) digits are identical and every conditioning event has positive probability. This contradiction proves infinite Markov order; order zero (independence) also fails.

## Verification

The accompanying standalone `verify.py` uses only exact integer and rational arithmetic for critical identities, plus floating-point logarithms for a supplementary sum-to-one check. It enumerates all \(4094\) nonempty binary words of lengths \(1\) through \(11\), checks reversed-word Möbius transpose identities and exact endpoint/cross-ratio equalities, verifies that the ordered cylinders tile \([1/3,1]\) at each depth, and checks the all-zero endpoint formula up to length \(59\). It also independently checks the transfer-operator identity at rational test points. Executing it returned `VERIFY_OK 4094`. These finite checks are not an infinite proof; the algebraic Steps 1–4 supply that proof.

## Relationship to prior work

Kraaikamp and Langeveld, *Invariant measures for continued fraction algorithms with finitely many digits* (2016), introduce the precise flipped map in their equation (3), and in Section 2.1.1 obtain the invariant density from its natural extension. Those objects are used here with attribution. Their article focuses on invariant density, entropy, and matching; its inspected text does not give the finite-word reversal identity or the all-zero infinite-order obstruction.

Dajani, Hensley, Kraaikamp and Masarotto, *Arithmetic and ergodic properties of 'flipped' continued fraction algorithms* (2012), develop the general flipped-algorithm framework, ergodicity, arithmetic and invariant-measure questions. Their inspected full article does not assert this two-symbol word-reversal law. General matrix transposition principles may have analogues elsewhere in continued-fraction theory, but an analogue is not, without a verified specialization, an implication of the exact result here. Classical stationary digit frequencies and two-dimensional natural extensions alone do not imply word reversibility for an arbitrary full-branch transformation.

## Limitations

This theorem does not claim that the underlying interval dynamics are invertible, that the digit process is independent, or that every generalized flipped expansion is symbolically reversible. It concerns the stated invariant initialization; no mixing-rate, central-limit, or entropy-rate formula is asserted. The closest-literature check cannot exclude an unpublished or unindexed equivalent derivation, and publication priority requires independent specialist review. The exact finite-word identity and its non-Markov consequence do not rely on numerical extrapolation.

## References

1. C. Kraaikamp and N. Langeveld, *Invariant measures for continued fraction algorithms with finitely many digits*, arXiv:1606.05099v1 (16 June 2016), Sections 2.1 and 2.1.1. https://arxiv.org/abs/1606.05099
2. K. Dajani, D. Hensley, C. Kraaikamp and V. Masarotto, *Arithmetic and ergodic properties of 'flipped' continued fraction algorithms*, Acta Arithmetica 153 (2012), 51–79. DOI: 10.4064/aa153-1-4. https://doi.org/10.4064/aa153-1-4
