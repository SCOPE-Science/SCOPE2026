# Exactly two exceptional characteristics for triple concurrence of Fermat-quartic bitangents

## Finding
Let \(k\) be algebraically closed of characteristic \(p\ge5\), and let \(C\subset\mathbb P^2_k\) be the smooth Fermat quartic \(X^4+Y^4+Z^4=0\). Among intersections of its 28 distinct geometric bitangent lines, write \(n_j\) for the number of geometric points incident with exactly \(j\) distinct lines. Then
\[
(n_2,n_3,n_4)=\begin{cases}
(240,16,15),&p=5,\\
(144,48,15),&p=17,\\
(288,0,15),&p\notin\{5,17\}.
\end{cases}
\]
There are no intersections of multiplicity at least five. Consequently, the bitangent incidence combinatorics changes from its characteristic-zero pattern in precisely two characteristics \(p\ge5\), namely five and seventeen.

## Assumptions and scope
The base field is algebraically closed of prime characteristic at least five; an intersection point is a geometric projective point, rather than necessarily a prime-field rational point. A bitangent may have two distinct contact points or one contact point of multiplicity four. The arrangement comprises the 28 distinct bitangent lines and not the quartic itself. The claim excludes characteristics two and three.

Fix a primitive eighth root of unity \(\zeta\) in \(k\). The 28 lines are the following explicit list, with each indicated pair of indices varying independently:
\[
X-\alpha Y=0,\quad X-\alpha Z=0,\quad Y-\alpha Z=0\qquad(\alpha^4=-1),
\]
\[
X+\mu Y+\nu Z=0\qquad(\mu^4=\nu^4=1).
\]
There are twelve lines in the first group and sixteen in the second. The coordinates are homogeneous and all roots of unity are geometric.

## Proof
**Exhaustion of bitangents.** The quartic is smooth because its partial derivatives have no common projective zero for \(p\ge5\). Each line \(X-\alpha Y=0\) with \(\alpha^4=-1\) restricts the quartic to \(Z^4=0\), hence is a hyperflex bitangent; likewise for permutations of coordinates. For \(X+\mu Y+\nu Z=0\), use \(U=\mu Y\) and \(V=\nu Z\). The restricted quartic becomes
\[
(U+V)^4+U^4+V^4=2(U^2+UV+V^2)^2.
\]
The quadratic has discriminant \(-3\), hence two distinct roots in every characteristic \(p\ge5\), giving two double contacts. The 28 displayed lines are distinct for all such characteristics. By the classical count of odd theta characteristics, a smooth nonhyperelliptic genus-three curve in characteristic different from two has precisely 28 geometric bitangents (including hyperflexes). Hence this list is exhaustive.

**Characteristic-independent determinant sieve.** Lift the line coefficients to the cyclotomic integer ring \(\mathbb Z[\zeta_8]\), where \(\zeta_8^4=-1\). For each of the \(\binom{28}{3}=3276\) unordered triples, form the determinant \(\delta\) of their coefficient rows and reduce it to the unique basis expression
\[
\delta=a_0+a_1\zeta_8+a_2\zeta_8^2+a_3\zeta_8^3,
\quad a_i\in\mathbb Z.
\]
Its absolute field norm is
\[
N(\delta)=(a_0^2-a_2^2+2a_1a_3)^2+(2a_0a_2-a_1^2+a_3^2)^2.
\]
This follows by multiplying first the conjugate expressions \(\delta(\zeta_8)\) and \(\delta(-\zeta_8)\) in the Gaussian integers, then multiplying their complex conjugates. Exact six-term determinant expansion produces the following *complete* norm histogram; each entry is \((N,\text{number of triples})\):
\[
\begin{array}{c|rrrrrrrrrrrrr}
N&0&1&2&4&8&9&16&17&32&36&64&256&400\\\hline
\#&60&384&64&864&384&192&560&192&96&192&192&64&32
\end{array}
\]
The counts sum to 3276. Every nonzero norm has prime factors among \(2,3,5,17\). In any characteristic \(p\ge5\) other than five or seventeen, every originally nonzero determinant remains nonzero: a zero determinant after reduction would force its integer field norm to vanish modulo \(p\). Conversely, every identically zero determinant remains zero. Thus the rank-three dependence pattern, and hence the whole projective intersection incidence structure of the 28 pairwise distinct lines, is constant in every characteristic \(p\ge5\), \(p\ne5,17\).

**The exceptional fields and intersection counts.** The eighth roots of unity lie in \(\mathbb F_{p^2}\) for every odd prime \(p\), because \(8\mid p^2-1\). Accordingly, all 28 lines and all pairwise intersection points are defined over \(\mathbb F_{p^2}\). It suffices to enumerate normalized nonzero cross-products of all 378 pairs of coefficient rows and, for each distinct resulting projective point, count incident lines by evaluating all 28 linear forms. This complete exact finite-field enumeration gives
\[
\begin{array}{c|rrrr|r}
p&n_2&n_3&n_4&n_{\ge5}&\sum_j\binom{j}{2}n_j\\\hline
5&240&16&15&0&378\\
17&144&48&15&0&378\\
7&288&0&15&0&378
\end{array}
\]
The row at \(p=7\), together with determinant-pattern invariance established above, proves the asserted counts for *every* \(p\ge5\) other than five and seventeen. The two exceptional rows prove the remaining cases. The equality of the weighted pair count with 378 verifies that every pair of distinct lines was accounted for. This completes the proof.

## Verification
Run `python verify.py` with Python 3 and its standard library only. The script generates all 28 coefficient rows, exhaustively enumerates all 3276 triple determinants in \(\mathbb Z[\zeta_8]\), computes every absolute norm with exact integers, checks the complete histogram, and enumerates all geometric pair-intersection points in \(\mathbb F_{p^2}\) for \(p\in\{5,7,17\}\) using exact modular arithmetic. It checks distinctness of all line pairs and the pair-count identity \(\sum_{j\ge2}\binom j2 n_j=378\). The program returned `VERIFY_OK`; its finite enumerations are exhaustive because every required line and intersection point is defined over the finite extension used.

## Relationship to prior work
Janasz–Pokora–Zieliński [1, Proposition 3.2] computed \(288\) ordinary double points and \(15\) quadruple points for the 28 bitangents of the Dyck/Fermat quartic over \(\mathbb C\). They explicitly work over the complex numbers [1, Introduction]. The present theorem uses that same natural geometric arrangement but studies its reduction to every prime characteristic at least five and finds two characteristic-specific triple-concurrence jumps not implied by their complex incidence counts. Ottaviani's account [2] describes the general theta-characteristic and bitangent geometry and presents the Fermat quartic as an example; it does not provide this arithmetic incidence sieve or these exceptional-prime counts.

## Limitations
No conclusion is made in characteristic two or three. The proof uses a complete finite determinant computation; its small input and exact algorithms are supplied rather than an independent symbolic classification of determinant orbits. The precise arithmetic incidence result may have appeared in unindexed classical or computational literature despite the comparisons reported separately. No claim is made about an arbitrary plane quartic or an arbitrary member of Ciani's pencil.

## References
[1] M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514, originally posted 2023-08-31; especially Section 3 and Proposition 3.2.

[2] G. Ottaviani, *Effective methods for plane quartics, their theta characteristics and the Scorza map*, arXiv:2403.19599 (2024); bitangents, odd theta characteristics, and the Fermat quartic example.
