# Rank gaps and an automorphism-density transition in finite Heisenberg Lie algebras

## Finding

Let \(q\) range over prime powers and let \(m\ge1\). Write \(H_m(q)=V\oplus\mathbb F_q z\) for the \((2m+1)\)-dimensional Heisenberg Lie algebra, where \(V\) carries a nondegenerate alternating bilinear form \(\omega\) and \([v,w]=\omega(v,w)z\). The generating polynomial for the ranks of all \(\mathbb F_q\)-linear Lie algebra endomorphisms \(\varphi:H_m(q)\to H_m(q)\) is

\[
\mathcal E_{m,q}(T)=q^{2m}(q-1)S_m(q)T^{2m+1}+\sum_{r=0}^{m} I_{m,r}(q)P_{m,r}(q)\left(q^rT^r+(q^{2m}-q^r)T^{r+1}\right),
\]

where

\[
I_{m,r}(q)=\prod_{i=0}^{r-1}\frac{q^{2(m-i)}-1}{q^{r-i}-1},\quad P_{m,r}(q)=\prod_{i=0}^{r-1}(q^{2m}-q^i),\quad S_m(q)=q^{m^2}\prod_{i=1}^{m}(q^{2i}-1).
\]

Empty products equal \(1\). These factors count isotropic image subspaces, surjections onto them, and symplectic automorphisms, respectively. Consequently every rank from \(0\) through \(m+1\) occurs, and the only possible larger rank is \(2m+1\): if \(m\ge2\), ranks \(m+2,\ldots,2m\) do not occur. The proportion of invertible elements of the finite endomorphism monoid has the following exact large-field limit, for each fixed \(m\):

\[
\lim_{q\to\infty}\frac{|\operatorname{Aut}(H_m(q))|}{|\operatorname{End}(H_m(q))|}=\begin{cases}1,&m=1,\\ \frac12,&m=2,\\0,&m\ge3.\end{cases}
\]

The limit is taken through prime powers. For instance,

\[
\mathcal E_{2,2}(T)=1+465T+15750T^2+37800T^3+11520T^5.
\]

## Assumptions and scope

Every finite field is permitted, including characteristic \(2\). A Lie algebra endomorphism means a linear bracket-preserving self-map, not necessarily invertible; its rank is the rank as a linear map on the full \((2m+1)\)-dimensional space. The displayed polynomial counts individual endomorphisms, not conjugacy classes. \(m\) is a positive integer; the density limit keeps \(m\) fixed. There is no assertion about a simultaneous limit in \(q\) and \(m\).

## Proof

Because \([H_m(q),H_m(q)]=\mathbb F_qz\), every endomorphism has a unique expression

\[
\varphi(v)=Av+f(v)z,\qquad\varphi(z)=\lambda z
\]

with \(A\in\operatorname{End}_{\mathbb F_q}(V)\), \(f\in V^*\), and \(\lambda\in\mathbb F_q\). Preservation of all brackets is equivalent to

\[
\omega(Av,Aw)=\lambda\omega(v,w)\quad\text{for all }v,w\in V.
\]

No further restriction involves \(f\), since \(z\) is central. This reduction remains valid in characteristic \(2\).

**Nonzero multiplier.** If \(\lambda\ne0\), the nondegeneracy of \(\omega\) forces \(A\) to be invertible; conversely every symplectic similitude is allowed. For each \(\lambda\in\mathbb F_q^\times\) choose a fixed similitude with multiplier \(\lambda\), so there are exactly \(|\operatorname{Sp}_{2m}(q)|=S_m(q)\) matrices per multiplier. Counting symplectic bases recursively proves \(S_m(q)=q^{m^2}\prod_{i=1}^m(q^{2i}-1)\). There are \(q^{2m}\) unrestricted choices of \(f\). Each such endomorphism has full rank \(2m+1\), giving the first summand.

**Zero multiplier.** If \(\lambda=0\), the image \(W=\operatorname{im}A\) is totally isotropic and has dimension \(0\le r\le m\). The number of such \(r\)-planes is \(I_{m,r}(q)\): the number of ordered linearly independent pairwise orthogonal \(r\)-tuples is

\[
\prod_{j=0}^{r-1}(q^{2m-j}-q^j),
\]

and division by \(|\operatorname{GL}_r(q)|=\prod_{j=0}^{r-1}(q^r-q^j)\) simplifies to the given product. For each fixed \(W\), the number of surjections \(V\to W\) is \(P_{m,r}(q)\). The full endomorphism has image spanned by the columns of \((A,f)\) in \(V\oplus\mathbb F_q z\); its rank is \(r\) exactly when \(f\) lies in the row space of \(A\), a dimension-\(r\) subspace of \(V^*\). This produces \(q^r\) choices with rank \(r\), and \(q^{2m}-q^r\) choices with rank \(r+1\). Summation proves the polynomial and positivity of every stated coefficient. In particular, the rank-zero coefficient is \(1\).

**Large-field comparison.** For fixed \(m\), the nonzero-multiplier term has leading degree in \(q\) equal to \(2m^2+3m+1\), with leading coefficient \(1\). The summand indexed by \(r\) in the singular total (set \(T=1\)) has leading degree

\[
D_m(r)=2m+4mr-\frac{3r^2-r}{2}.
\]

Indeed the isotropic Grassmannian has degree \(2mr-(3r^2-r)/2\), the surjection factor has degree \(2mr\), and \(f\) contributes \(2m\). For \(0\le r<m\), \(D_m(r+1)-D_m(r)=4m-3r-1>0\); thus the singular total has unique leading stratum \(r=m\), degree \((5m^2+5m)/2\), also with coefficient \(1\). The degree difference (singular minus invertible) is \((m-2)(m+1)/2\). The stated limiting proportions follow, including the equal-degree case \(m=2\), when both leading coefficients are \(1\).

## Verification

The standalone `verify.py` checks the formula without invoking its symplectic-plane parameter count in its brute-force branches. It directly enumerates all \(3\times3\) matrices representing linear maps for \(q=2,3,4\), checks the bracket relations, and computes ranks by finite-field elimination. For \(m=2\) over \(\mathbb F_2\), it enumerates all quotient maps and central functionals directly, checks the symplectic pairing relations and ranks by binary elimination. The complete dimension-five result is \(1,465,15750,37800,11520\) across ranks \(0,1,2,3,5\), respectively; the total is \(65536\). Further exact finite-product checks cover \(q\in\{2,3,4,5,7\}\) and \(1\le m\le7\). Run `python3 verify.py`; a successful run ends `VERIFY_OK_HEISENBERG_ENDOMORPHISM_RANKS`. Finite checks support, but do not replace, the preceding general proof.

## Relationship to prior work

Fisher, Gray and Hydon [1] construct automorphism groups of real Lie algebras of dimension at most five, including the three-dimensional Heisenberg example. This gives automorphism-side context, but not noninvertible endomorphism ranks, uniform finite-field counts, or the large-field transition. Rieck [2] counts prescribed-pairing vector configurations in finite symplectic spaces in odd characteristic. Those classical isotropic-frame counts supply a major input; no novelty is claimed for that component or for the classical order of the symplectic group. The combination with the central functional, its rank contribution, and the resulting full spectrum and asymptotic density are the specific claims here.

## Limitations

The formula describes one-parameter Heisenberg Lie algebras with one-dimensional center generated by brackets. It does not classify endomorphisms up to conjugation, multiplication in the endomorphism monoid, or extensions to other two-step nilpotent Lie algebras. The counting proof applies to all finite fields. A bibliographic risk remains that an equivalent formula is implicit in earlier symplectic-similitude monoid or Lie-endomorphism literature; no claim of globally certified priority or independent audit is made.

## References

[1] D. J. Fisher, R. J. Gray, and P. E. Hydon, *Automorphisms of real Lie algebras of dimension five or less*, arXiv:1303.3376v1 (first public version 2013-03-14), https://arxiv.org/abs/1303.3376.

[2] M. Q. Rieck, *Counting Configurations of Vectors in a Finite Vector Space with an Orthogonal, Symplectic or Unitary Geometry*, Journal of Combinatorial Mathematics and Combinatorial Computing **34** (2000), 23–32, https://combinatorialpress.com/jcmcc-articles/volume-034/counting-configurations-of-vectors-in-a-finite-vector-space-with-an-orthogonal-symplectic-or-unitary-geometry/.
