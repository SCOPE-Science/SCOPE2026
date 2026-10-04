# Paired domination of annihilating-ideal graphs of reduced rings with finite minimal spectrum

## Finding

Let \(R\) be a reduced commutative non-domain with identity and finitely many minimal prime ideals, \(m=|\operatorname{Min}(R)|\ge2\). Then the paired-domination number of its annihilating-ideal graph is \[\gamma_{pr}(\mathbb{AG}(R))=2\left\lceil \frac{m}{2}\right\rceil,\] equivalently \(m\) when \(m\) is even and \(m+1\) when \(m\) is odd.

This extends the parity formula previously proved for commutative Artinian rings to arbitrary reduced rings with finite minimal spectrum, including non-Artinian examples.

## Assumptions and scope

Let \(R\) be a commutative ring with identity. The annihilating-ideal graph \(\mathbb{AG}(R)\) has as vertices the nonzero ideals with nonzero annihilator; two distinct vertices \(I,J\) are adjacent exactly when \(IJ=(0)\). A paired-dominating set is a dominating set whose induced subgraph has a perfect matching.

Assume throughout that \(R\) is reduced, is not a domain, and
\[
\operatorname{Min}(R)=\{P_1,\ldots,P_m\},\qquad m\ge2.
\]
Because \(R\) is reduced,
\[
\bigcap_{i=1}^m P_i=(0).
\]

## Proof

For each \(i\), define
\[
A_i=\prod_{j\ne i}P_j.
\]
The ideal \(A_i\) is nonzero. Indeed, if \(A_i\subseteq P_i\), primality of \(P_i\) would force \(P_j\subseteq P_i\) for some \(j\ne i\), contradicting minimality and distinctness of the minimal primes. Also
\[
A_iP_i\subseteq\prod_{j=1}^mP_j\subseteq\bigcap_{j=1}^mP_j=(0),
\]
so both \(A_i\) and \(P_i\) are vertices.

If \(i\ne k\), then \(A_iA_k\) is contained in every minimal prime: \(A_k\subseteq P_i\), \(A_i\subseteq P_k\), and for every other \(P_j\) both products contain a factor from \(P_j\). Hence
\[
A_iA_k=(0).
\]
Thus \(D_0=\{A_1,\ldots,A_m\}\) induces a clique.

The set \(D_0\) totally dominates \(\mathbb{AG}(R)\). Let \(I\) be any vertex and choose \(0\ne x\in\operatorname{Ann}(I)\). Since the intersection of the minimal primes is zero, choose \(i\) with \(x\notin P_i\). For every \(y\in I\), the equality \(xy=0\in P_i\), together with primality of \(P_i\), implies \(y\in P_i\). Hence \(I\subseteq P_i\), and therefore \(IA_i=(0)\). If \(I=A_i\), another member of the clique supplies the required neighbor because \(m\ge2\).

We next prove the matching lower bound without assuming Artinianity. Each \(P_i\) is maximal among proper annihilating ideals. Suppose instead that \(P_i\subsetneq K\) for an annihilating ideal \(K\), and choose \(0\ne x\in\operatorname{Ann}(K)\) and \(y\in K\setminus P_i\). From \(xy=0\) and primality, \(x\in P_i\). For each \(j\ne i\), the ideal \(A_j\subseteq P_i\subseteq K\) is not contained in \(P_j\); choose \(z_j\in A_j\setminus P_j\). Then \(xz_j=0\) forces \(x\in P_j\). Hence \(x\in\bigcap_jP_j=(0)\), a contradiction.

Let \(D\) be any total dominating set. For each \(i\), choose \(J_i\in D\) adjacent to \(P_i\). Then \(P_i\subseteq\operatorname{Ann}(J_i)\). The annihilator is a proper annihilating ideal, so maximality gives
\[
\operatorname{Ann}(J_i)=P_i.
\]
Consequently \(J_i=J_k\) implies \(P_i=P_k\); therefore the \(J_i\) are distinct and every total dominating set has at least \(m\) vertices. Every paired-dominating set is total dominating and has even cardinality, so
\[
\gamma_{pr}(\mathbb{AG}(R))\ge2\left\lceil\frac m2\right\rceil.
\]

If \(m\) is even, the clique \(D_0\) has a perfect matching, so it is paired dominating and equality follows. If \(m\) is odd, then \(m\ge3\). The vertex \(P_1\) is distinct from every \(A_i\): for \(i=1\), equality would give \(P_1^2=(0)\), impossible in a reduced non-domain; for \(i\ne1\), choose \(j\notin\{1,i\}\), and \(A_i\subseteq P_j\), so \(P_1=A_i\) would contradict incomparability of distinct minimal primes. Now
\[
D_1=D_0\cup\{P_1\}
\]
is dominating. Match \(P_1\) with \(A_1\), and pair the remaining \(m-1\) vertices of the clique \(D_0\). Hence \(D_1\) is paired dominating of size \(m+1\), proving equality in the odd case.

## Verification

The proof is symbolic. The accompanying `verify.py` independently checks the finite semiprimitive model \(R=\mathbb F_2^m\), where nonzero proper ideals correspond to nonempty proper coordinate supports and adjacency is disjointness. It exhaustively rules out all smaller even paired-dominating sets for \(2\le m\le5\) and verifies the construction above. The output is:

```text
m=2 vertices=2 gamma_pr=2
m=3 vertices=6 gamma_pr=4
m=4 vertices=14 gamma_pr=4
m=5 vertices=30 gamma_pr=6
VERIFY_OK
```

These finite checks are corroborative only; the theorem for arbitrary reduced rings follows from the minimal-prime argument above.

## Relationship to prior work

Behboodi and Rakeei introduced \(\mathbb{AG}(R)\) and its basic structure in 2008. Chelvam and Selvakumar (2014) proved that for a commutative Artinian ring with \(n\ge2\) maximal ideals, the paired-domination number is \(n\) for even \(n\) and \(n+1\) for odd \(n\). Their standing hypothesis in the relevant section is Artinianity.

Nikandish, Maimani, and Kiani (2015) proved that for a reduced ring with finitely many minimal primes, the total domination number is the number of minimal primes in the nontrivial regime. Badie (2021) later recovered and extended the finite-minimal-spectrum total-domination statement through a topological treatment. The present result adds the perfect-matching constraint and proves that only the parity correction remains: the Artinian paired-domination formula persists for every reduced ring with finite minimal spectrum.

A 2024 paper by Visweswaran revisits domination and total domination for annihilating-ideal graphs of reduced rings; its stated scope and full-text terminology do not include paired domination.

Concrete non-Artinian examples include \(R=k[x,y]/(xy)\), for which \(m=2\) and \(\gamma_{pr}=2\), and \(R=k[x,y,z]/(xy,xz,yz)\), for which \(m=3\) and \(\gamma_{pr}=4\).

## Limitations

Reducedness and finiteness of \(\operatorname{Min}(R)\) are essential to this proof. The theorem does not classify paired domination for nonreduced rings with infinitely many minimal primes. The 2014 Artinian theorem overlaps on the reduced Artinian subclass; the contribution here is the extension beyond Artinianity. Targeted searches did not locate an earlier finite-minimal-spectrum paired-domination theorem, but an unindexed source remains a residual originality risk.

## References

1. M. Behboodi and Z. Rakeei, “The Annihilating-Ideal Graph of Commutative Rings I,” arXiv:0808.3187, first posted 2008-08-23.
2. T. Tamizh Chelvam and K. Selvakumar, “Central Sets in the Annihilating-Ideal Graph of Commutative Rings,” *Journal of Combinatorial Mathematics and Combinatorial Computing* 88 (2014), 277–288.
3. R. Nikandish, H. R. Maimani, and S. Kiani, “Domination Number in the Annihilating-Ideal Graphs of Commutative Rings,” *Publications de l’Institut Mathématique* 97(111) (2015), 225–231. DOI: 10.2298/PIM140222001N.
4. M. Badie, “Notes on the Zero-Divisor Graph and Annihilating-Ideal Graph of a Reduced Ring,” *Analele Universităţii Ovidius Constanţa - Seria Matematică* 29(2) (2021), 51–70. DOI: 10.2478/auom-2021-0018.
5. S. Visweswaran, “Some Remarks on the Dominating Sets of the Annihilating-Ideal Graph of a Commutative Ring,” *Discussiones Mathematicae General Algebra and Applications* 44(2) (2024), 383–412. DOI: 10.7151/dmgaa.1458.
