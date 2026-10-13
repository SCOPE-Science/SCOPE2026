# Fixed-space and element-orbit spectra of fourth-order substitution jets

## Finding
Let \(q=p^e\) be any prime power and let \(A_q=\mathbb F_q[t]/(t^5)\). For every integer \(j\), let \(N_j(q)\) denote the number of \(\mathbb F_q\)-algebra automorphisms \(\phi\) of \(A_q\) satisfying \(\dim_{\mathbb F_q}\ker(\phi-I)=j\). Define the root-of-unity correction terms
\[
 r_3=\gcd(3,q-1)-1,\qquad r_4=\gcd(4,q-1)-\gcd(2,q-1).
\]
They respectively count the nonidentity cube roots and primitive fourth roots of unity in \(\mathbb F_q\). All counts not included in the following tables are zero.

If \(p\ge5\), then
\[
\begin{array}{c|ccccc}
 j&1&2&3&4&5\\\hline
 N_j(q)&(q-3-r_3-r_4)q^3&2q^2(q-1)+(r_3+r_4)q^3&2q^2-q&q-1&1
\end{array}
\]
and the automorphism group has exactly \(q(7+r_3+r_4)\) orbits on the underlying set of \(A_q\).

If \(p=3\), then
\[
\begin{array}{c|ccccc}
 j&1&2&3&4&5\\\hline
 N_j(q)&(q-3-r_4)q^3&(q^3-q^2)+r_4q^3&q^3+q^2-q&q-1&1
\end{array}
\]
and the number of element-orbits is \(q(q+r_4+6)\).

If \(p=2\), then
\[
\begin{array}{c|ccccc}
 j&1&2&3&4&5\\\hline
 N_j(q)&(q-2-r_3)q^3&r_3q^3&(q-1)q^2&q^2-1&1
\end{array}
\]
and the number of element-orbits is \(q(2q+r_3+3)\).

Each distribution sums to \((q-1)q^3\), the exact number of automorphisms. A structural phase transition follows: the element-orbit count is linear in \(q\) for characteristics at least five but quadratic in \(q\) for characteristics two and three. The corrections \(r_3,r_4\) record genuine multiplier resonances, not exceptional individual field sizes.

## Assumptions and scope
The algebra is **unital**, commutative, associative, and defined over the named base field; only base-field-linear automorphisms fixing \(1\) are counted, not field-semilinear maps. Its dimension is five. The automorphism group acts on **all** \(q^5\) elements of \(A_q\) by substitution. Its radical \((t)\) has dimension four and is invariant. There are no assumptions on primality beyond \(q=p^e\), and all formulas apply equally to nonprime fields. The fixed dimension includes the compulsory one-dimensional fixed subspace of scalar constants.

The jet order \(4\) is natural: substitution modulo \(t^5\) retains a first simultaneous occurrence of a repeated \(1\)-eigenvalue in even degrees at multiplier \(-1\) and a degree-four constraint involving the square of the quadratic coefficient. This is the first truncated one-variable jet where that particular quadratic resonance affects the full fixed-space census.

## Proof
**1. Complete automorphism parametrization.** Since the maximal ideal \((t)\) and its powers are characteristic and \((t)/(t^2)\) is one-dimensional, any automorphism is uniquely determined by
\[
 \phi(t)=at+bt^2+ct^3+dt^4\pmod{t^5},\qquad a\in\mathbb F_q^\times,\quad b,c,d\in\mathbb F_q.
\]
Conversely each such substitution is invertible: its matrix on \((t)\) is triangular with nonzero diagonal \(a,a^2,a^3,a^4\); hence the induced linear map on \(A_q\) is invertible, and its inverse is an algebra map. Thus \(|\operatorname{Aut}(A_q)|=(q-1)q^3\).

**2. The exact fixed matrix.** Relative to \((t,t^2,t^3,t^4)\), the restriction of \(\phi\) to the radical has matrix
\[
M(a,b,c,d)=
\begin{pmatrix}
a&0&0&0\\
b&a^2&0&0\\
c&2ab&a^3&0\\
d&b^2+2ac&3a^2b&a^4
\end{pmatrix}.
\]
For every multiplier and every triple of coefficients, exactly
\[
\dim\operatorname{Fix}(\phi)=1+\dim\ker(M-I_4)=5-\operatorname{rank}(M-I_4)
\]
because the constant direction is fixed independently of the radical.

**3. Multiplier strata away from one.** The diagonal entries of \(M-I_4\) are \(a-1,a^2-1,a^3-1,a^4-1\). If none vanishes, the radical has no fixed vector, so the full fixed dimension is one. For \(a\ne1,-1\), at most one diagonal entry vanishes, and this happens exactly for a nonidentity cube root or primitive fourth root of unity; the corresponding radical fixed dimension is one, regardless of \((b,c,d)\). These yield \((r_3+r_4)q^3\) automorphisms with full fixed dimension two. For odd characteristic, the remaining special multiplier \(a=-1\) has two vanishing diagonal entries. The first fixed-coordinate equation makes the coefficient of \(t\) zero; the degree-three equation gives the coefficient of \(t^3\) as \(-b\) times that of \(t^2\). The degree-four equation then becomes
\[
 -2(b^2+c)\,x_2=0.
\]
Hence, in odd characteristic, \(a=-1\) contributes exactly \(q^2\) automorphisms with full fixed dimension three (those having \(c=-b^2\), with arbitrary \(d\)) and \(q^3-q^2\) with full fixed dimension two. In characteristic two \(-1=1\), so this stratum is absent.

**4. The identity-multiplier stratum.** Set \(a=1\). The first row of \(M-I_4\) vanishes; its remaining potentially nonzero \(3\times3\) block is
\[
 R(b,c,d)=\begin{pmatrix}
b&0&0\\
c&2b&0\\
d&b^2+2c&3b
\end{pmatrix}.
\]
If \(p\ge5\), its ranks are \(3\) when \(b\ne0\), \(2\) when \(b=0,c\ne0\), \(1\) when \(b=c=0,d\ne0\), and \(0\) otherwise. The corresponding numbers of automorphisms are \((q-1)q^2\), \((q-1)q\), \(q-1\), and \(1\).

If \(p=3\), the same four cases have respective ranks \(2,2,1,0\), because \(3b=0\) while \(2\ne0\). If \(p=2\), the ranks are \(2,1,1,0\), because \(2=0\) and \(3=1\). In all characteristics these ranks are independent of \(d\) except in the last two cases stated. The numbers of coefficient triples remain \((q-1)q^2,(q-1)q,q-1,1\). Summing the multiplier strata proves all five entries in the three displayed distributions. In characteristic three, no nonidentity cube root of unity exists because \(3\) does not divide \(q-1\); in characteristic two no distinct multiplier \(-1\) exists.

**5. Element orbits.** Burnside's orbit-counting identity, applied to the action on the underlying set of \(A_q\), states
\[
 \#(A_q/\operatorname{Aut}(A_q))
 =\frac{1}{(q-1)q^3}\sum_{j=1}^{5}N_j(q)q^j.
\]
Every fixed subspace with dimension \(j\) has exactly \(q^j\) elements. Substituting the proved distributions and simplifying gives, respectively, \(q(7+r_3+r_4)\), \(q(q+r_4+6)\), and \(q(2q+r_3+3)\). As a separate normalization, summing every \(N_j\) gives the automorphism order \((q-1)q^3\). These algebraic identities remain valid at the smallest eligible fields, where some strata are empty.

## Verification
The standalone standard-library program `artifacts/verify.py` constructs explicit prime and extension finite fields and computes \(M-I_4\) ranks by Gaussian elimination. Running `python3 artifacts/verify.py` exhaustively tests every automorphism for \(q\in\{2,3,4,5,7,8,9,11,13,16\}\), compares all multiplicities with the closed formulas, and verifies the Burnside sums. It also enumerates the actual element orbits, without relying on Burnside, for \(q=2,3,4\); the resulting orbit totals are \(14,27,52\). The script ends with `VERIFY_OK`. The proof is symbolic for all prime powers; finite checks verify implementations and small-field boundaries, not infinitely many instances.

## Relationship to prior work
Jennings' 1954 study of substitution groups establishes the formal-substitution framework and its finite quotients, including explicit truncation/composition rules and the larger full group with nontrivial linear coefficient. Chinburg and Symonds (2010) study torsion in the Nottingham group, exhibiting an order-four formal substitution in characteristic two. Lubin (2011) studies finite-order conjugacy and ramification for the Nottingham group. These works motivate the natural finite jets and their special-characteristic behavior; none of their inspected statements gives the above fixed-space-fiber counts for the full linear-coefficient extension or the three Burnside orbit formulas.

Published work on automorphisms of truncated coordinate-cross algebras explicitly describes \(J_d(k)=\operatorname{Aut}_k(k[t]/(t^d))\) and its order \((q-1)q^{d-2}\) over \(\mathbb F_q\). This supplies the group-order normalization for the present \(d=5\) case but not the rank-fiber distribution of the natural representation; group order alone does not determine it. Published work on truncated Nottingham braces determines socle filtrations and multipermutation levels, a different invariant of a tangent-to-identity substitution group. Recent studies of substitution-group exponents and presentations likewise concern different invariants. Thus the original claim here is the **complete fixed-space distribution and consequent element-orbit count**, not the classical substitution parametrization.

## Limitations
The theorem concerns only the length-five univariate algebra, not higher truncation lengths, semilinear substitutions, classification of group conjugacy classes, or orbit-size partitions. It does not assert independence from classical substitution structure; the structural parametrization is known and is explicitly credited. Published equivalent tables could be indexed under truncated power-series modules or jet-group representations rather than the searched terminology. Some recent preprints were accessible only by abstract, so exact noncoverage of their full text cannot be certified; this residual originality risk does not substitute for an independent literature audit.

## References
1. S. A. Jennings, *Substitution Groups of Formal Power Series*, Canadian Journal of Mathematics **6** (1954), 325–340. DOI: 10.4153/CJM-1954-031-9. Full publisher PDF inspected (substitution/quotient constructions, §§1–5, especially Theorems 1.4, 2.2 and discussion around p. 338).
2. T. Chinburg and P. Symonds, *An element of order 4 in the Nottingham group at the prime 2*, arXiv:1009.5135v1, first posted 26 September 2010; primary MSC 20F29. Full arXiv HTML inspected, including Theorem 1.1 and literature discussion.
3. J. Lubin, *Torsion in the Nottingham group*, Bulletin of the London Mathematical Society **43** (2011), 547–560, DOI: 10.1112/blms/bdq120; the author-hosted full manuscript at https://www.math.brown.edu/jlubin/TorsInNott.pdf was inspected.
4. A. D'Alessandro and F. Szechtman, *Substitution groups of formal power series*, arXiv:2606.11461 (2026), abstract inspected; exponent results, full text not obtained in the available sources.
5. F. Szechtman, *A power-commutator presentation for the group of truncated polynomials under substitution*, arXiv:2610.01469 (2026), abstract inspected; full preprint retrieval did not succeed.
6. *Automorphisms of truncated coordinate-cross algebras over arbitrary fields*, publicly posted mathematical finding, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-automorphisms-of-truncated-coordinate-cross-algebras-over-arbitr--625ba30274cb; full RESULT.md inspected.
7. *Truncated Nottingham braces attain maximal multipermutation level at every odd prime*, publicly posted mathematical finding, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-truncated-nottingham-braces-attain-maximal-multipermutation-leve--fdfe4aefbe51; full RESULT.md inspected.
