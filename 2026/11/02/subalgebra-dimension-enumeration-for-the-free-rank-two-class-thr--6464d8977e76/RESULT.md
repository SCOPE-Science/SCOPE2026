# Subalgebra-dimension enumeration for the free rank-two class-three Lie algebra

## Finding

For every finite field \(\mathbb F_q\), let \(L\) be the five-dimensional free nilpotent Lie algebra of rank two and class three. For \(0\le k\le5\), let \(s_k(q)\) be the number of \(k\)-dimensional Lie subalgebras (including zero and the whole algebra). Its dimension-generating polynomial is

\[
P_q(t)=1+(q^4+q^3+q^2+q+1)t+(q^4+2q^3+2q^2+q+1)t^2+(q^3+2q^2+q+1)t^3+(q+1)t^4+t^5.
\]

In particular, the three-dimensional subalgebras comprise exactly \(q^2+q+1\) abelian subalgebras and \(q^2(q+1)\) nonabelian subalgebras; the nonabelian subalgebras are all isomorphic to the three-dimensional Heisenberg Lie algebra. Thus the total number of subalgebras is \(2q^4+4q^3+5q^2+4q+6\). Uniformly choosing a subalgebra, dimensions one and two each have limiting probability \(1/2\) as \(q\to\infty\) through prime powers. Uniformly choosing a three-dimensional subalgebra, the probability of nonabelian type tends to one.

## Assumptions and scope

Choose the ordered basis \(x,y,z,u,v\), and declare the only nonzero basic brackets to be \([x,y]=z\), \([x,z]=u\), \([y,z]=v\), together with those required by skew-symmetry and \([a,a]=0\). The span \(Z=\langle u,v\rangle\) is its two-dimensional center; \(Q=L/Z\) is the three-dimensional Heisenberg Lie algebra with basis \(\bar x,\bar y,\bar z\) and relation \([\bar x,\bar y]=\bar z\). All subalgebras are linear subspaces closed under the Lie bracket over the *whole* field \(\mathbb F_q\). No characteristic restriction is used, including characteristic two.

## Proof

Let \(\pi:L\to Q\) be the quotient map. For any subalgebra \(S\le L\), set \(A=\pi(S)\le Q\) and \(K=S\cap Z\le Z\). A subspace \(S\) with these prescribed \(A,K\) is a graph of a unique linear map \(f:A\to Z/K\), once the natural vector-space complements are fixed. This contributes \(q^{(\dim A)(2-\dim K)}\) candidate subspaces. Centrality of \(Z\) implies that all such candidates are subalgebras if and only if the central bracket components of lifts of every pair in \(A\) lie in \(K\), with the projected bracket lying in \(A\). In the cases below, the projected brackets are either zero or have a lift belonging to every candidate, and the criterion reduces to the stated condition on \(K\).

**Case \(\dim A=0\).** Here \(S=K\) is any subspace of the two-dimensional center. These contribute one subalgebra of dimension zero, \(q+1\) of dimension one, and one of dimension two.

**Case \(\dim A=1\).** All \(q^2+q+1\) lines of \(Q\) are abelian Lie subalgebras. Since alternating brackets vanish on each such line, any \(K\le Z\) and any map \(A\to Z/K\) yield a subalgebra. For \(\dim K=0,1,2\), respectively, the numbers are \((q^2+q+1)q^2\) of dimension one, \((q^2+q+1)(q+1)q\) of dimension two, and \(q^2+q+1\) of dimension three. The last are abelian because they have only one noncentral generator.

**Case \(\dim A=2\).** Every two-dimensional Lie subalgebra of \(Q\) must contain \(\bar z\): otherwise, two independent vectors with independent images in \(Q/\langle\bar z\rangle\) have nonzero bracket \(\bar z\) outside the plane. Thus \(A=\langle\bar z, a\bar x+b\bar y\rangle\) with a projective direction \([a:b]\in\mathbb P^1(\mathbb F_q)\), giving \(q+1\) choices. For a subalgebra \(S\) lifting \(A\), brackets with lifts of \(\bar z\) are \(a u+b v\), a nonzero central vector independent of the chosen lifts. Necessarily \(K\) contains the line \(\langle a u+b v\rangle\); conversely this is sufficient because all other brackets of the two generators vanish. Hence either \(K=\langle a u+b v\rangle\), yielding \(q^2\) graph maps and \(q^2(q+1)\) three-dimensional nonabelian subalgebras, or \(K=Z\), yielding exactly \(q+1\) four-dimensional subalgebras. Each three-dimensional nonabelian subalgebra has central derived algebra of dimension one and is Heisenberg.

**Case \(\dim A=3\).** Any surjective subalgebra \(S\to Q\) contains lifts of \(\bar x,\bar y,\bar z\). Their brackets with the lift of \(\bar z\) yield both \(u\) and \(v\), so \(K=Z\). Hence \(S=L\), the sole subalgebra of dimension five.

Summing all cases gives the claimed six coefficients, with no overlaps because \((A,K)\) are intrinsically determined by \(S\). Their total is \(2q^4+4q^3+5q^2+4q+6\). The leading terms in dimensions one and two are each \(q^4\); all others have smaller degree, proving their \(1/2\) limiting probabilities. Among three-dimensional subalgebras, the ratio of the nonabelian count \(q^2(q+1)\) to \(q^3+2q^2+q+1\) tends to one.

## Verification

The companion `verify.py` constructs all vector subspaces in canonical reduced-row-echelon form, directly tests bracket closure, and counts the abelian three-dimensional subalgebras. It uses explicit field operations over \(\mathbb F_2\), \(\mathbb F_3\) and \(\mathbb F_4\), where the last is implemented as a quotient of a quadratic polynomial ring. Running `python3 verify.py` outputs `VERIFY_OK` after these three exhaustive enumerations. Their dimension profiles are respectively \((1,31,43,19,3,1)\), \((1,121,157,49,4,1)\), and \((1,341,421,101,5,1)\). These finite computations independently cross-check the exact formulas; the proof above establishes all prime powers.

## Relationship to prior work

Lee's 2019 thesis and subsequent paper on finite-field Lie-algebra zeta functions develop the relevant finite-field enumeration methodology. Theorem 3.7 of the published preprint gives the **ideal** zeta polynomial of this same five-dimensional free nilpotent Lie algebra, not the subalgebra polynomial established here. Its other nilpotent subalgebra enumerations concern distinct maximal-class Lie algebras. Eick and Moede give algorithms for general finite-field Lie subalgebras, but their enumerated families are simple Lie algebras over \(\mathbb F_2\), not this unrestricted formula. The older local subring zeta archive explicitly lists the same integral Lie ring; it concerns finite-index subrings of an integral Lie ring, not a dimension-refined census of its finite-field linear subalgebras. Its linked source PDF was inaccessible during the literature check, so possible derivations from that source remain unresolved.

## Limitations

The result is a complete enumeration for one distinguished five-dimensional free class-three Lie algebra, not a formula for arbitrary free nilpotent Lie algebras. There is no assertion of independent audit or global priority. The inaccessible older subring-zeta PDF and Lee's 2019 thesis full text present residual priority risks even though the accessible 2020 paper covers only ideals for this object. The verifier checks only three finite fields; validity for all prime powers rests on the algebraic proof, not on extrapolation of computations.

## References

1. Seungjai Lee, *Variations on the theme of zeta functions of groups and rings*, University of Oxford doctoral thesis, publicly deposited 23 October 2019, DOI: `10.5287/ora-nzqowgpgw`.
2. Seungjai Lee, *Zeta functions of \(\mathbb{F}_p\)-Lie algebras and finite p-groups*, arXiv:2010.02268, first publicly posted 5 October 2020; arXiv HTML version 3, Section 3.1.4, Theorem 3.7.
3. Bettina Eick and Tobias Moede, *Computing subalgebras and Z2-gradings of simple Lie algebras over finite fields*, arXiv:2205.03155, first publicly posted 6 May 2022, Sections 3–4.
4. *Zeta Functions of Lie Rings Archive*, `https://www.lack-of.org.uk/zfarchive/`, class-three table, \(F_{3,2}\) row; older finite-index subring entry, source PDF not inspected.
