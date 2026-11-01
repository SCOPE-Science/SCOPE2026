# Fundamental groups and torsion of cyclic three-term progression complexes

## Finding
For every prime \(p\ge5\), the canonical cyclic three-term-progression simplicial complex has a fundamental group that is a free product of an explicitly ranked free group and explicitly ordered cyclic groups:
\[
\pi_1(K_p)\cong F_{(p-1)(q_p-1)}*\underbrace{C_{m_p}*\cdots*C_{m_p}}_{q_p\text{ factors}}.
\]
Its integral homology is
\[
H_1(K_p;\mathbb Z)\cong\mathbb Z^{(p-1)(q_p-1)}\oplus(\mathbb Z/m_p)^{q_p},\qquad
H_2(K_p;\mathbb Z)\cong\mathbb Z^{q_p(p-1)},
\]
and its higher homology vanishes. As usual, \(H_0(K_p;\mathbb Z)\cong\mathbb Z\). Here \(C_1\) denotes the trivial group and \(\mathbb Z/1\) denotes the zero group.

## Assumptions and scope
Let \(p\ge5\) be any prime. Define \(K_p\) as the abstract simplicial complex with vertex set \(\mathbb F_p\) and facets exactly the unordered sets \(\{a,a+d,a+2d\}\), where \(a\in\mathbb F_p\) and \(d\in\mathbb F_p^*\). This is the *facet complex* of the cyclic three-term-progression hypergraph, not its hypergraph independence complex. Define \(h_p\) as the least positive integer with \(2^{h_p}\equiv\sigma_p\pmod p\) for one sign \(\sigma_p\in\{1,-1\}\), and set
\[
q_p=\frac{p-1}{2h_p},\qquad N_p=2^{h_p}-\sigma_p,\qquad m_p=\frac{N_p}{p}.
\]
The sign is unambiguous because \(p\) is odd. Both \(q_p\) and \(m_p\) are positive integers: the classes of nonzero residues modulo sign form cycles of signed multiplication by two of length \(h_p\), and \(p\mid N_p\). Let \(F_r\) be the free group on \(r\) generators, and \(C_m\) the cyclic group of order \(m\).

## Proof
**1. Face enumeration and a free covering.** Two different three-term progressions have the same unordered vertex set only when their middle terms coincide (a second possible midpoint would imply \(3d=0\), impossible for \(p\ge5\)). For a given \(d\), reversal identifies \((a,d)\) with \((a+2d,-d)\). Thus there are precisely \(p(p-1)/2\) distinct triangular facets. For any distinct \(u,v\in\mathbb F_p\), the triple \(\{u,(u+v)/2,v\}\) is a facet, so the one-skeleton is complete and has \(p(p-1)/2\) edges. Consequently, \(K_p\) has face vector \((p,p(p-1)/2,p(p-1)/2)\) and Euler characteristic \(\chi(K_p)=p\).

The additive group \(A=(\mathbb F_p,+)\) acts on \(K_p\) by translations. No nonidentity translation can stabilize a nonempty simplex setwise: its only vertex orbit has length \(p\), strictly exceeding every simplex size. Hence the action is free on the realization, and \(K_p\to Y_p=|K_p|/A\) is a regular \(p\)-sheeted covering of a finite CW complex. The quotient has one vertex, one oriented edge \(e_d\) for each step modulo sign (with convention \(e_{-d}=e_d^{-1}\)), and one triangular two-cell for each such step. The oriented triangle \((a,a+d,a+2d)\) has attaching word \(e_de_de_{2d}^{-1}\). Therefore
\[
\pi_1(Y_p)=\langle e_d\ (d\in\mathbb F_p^*): e_{-d}=e_d^{-1},\ e_{2d}=e_d^2\rangle.
\]
These are all the relations, because the quotient CW structure has exactly these cells.

**2. Elimination of signed-doubling orbits.** The permutation \([d]\mapsto[2d]\) of \(\mathbb F_p^*/\{\pm1\}\) has every orbit of length \(h_p\) and hence \(q_p\) orbits. In each orbit, choose a representative \(d\) and successively eliminate the other edge generators using \(e_{2d}=e_d^2\). The sole remaining relation is \(e_d^{2^{h_p}}=e_d^{\sigma_p}\), equivalently \(e_d^{N_p}=1\). Distinct signed-doubling orbits have disjoint relations. It follows, by explicit presentation eliminations, that
\[
\pi_1(Y_p)\cong C_{N_p}*\cdots*C_{N_p}\quad(q_p\text{ factors}).
\]

**3. Recover the covering kernel.** The covering monodromy map \(\rho:\pi_1(Y_p)\to A\cong C_p\) sends the edge \(e_d\) to translation by \(d\). Each free-product factor maps onto \(A\) (its chosen \(d\) is nonzero), and \(p\mid N_p\). The group \(\pi_1(K_p)\) is the kernel of \(\rho\).

Apply the Bass–Serre description of a free product to the star-shaped graph of groups: a central trivial vertex, one peripheral vertex with group \(C_{N_p}\) for each of the \(q_p\) factors, and trivial edge groups. The subgroup \(\ker\rho\), of index \(p\), has quotient graph with \(p\) lifts of the central vertex, exactly one lift of each peripheral vertex, and \(p\) lifted edges for each peripheral factor. This graph is connected, with \(p+q_p\) vertices and \(pq_p\) edges; its cycle rank is
\[
pq_p-(p+q_p)+1=(p-1)(q_p-1).
\]
Each peripheral stabilizer in the kernel is precisely the subgroup \(C_{N_p/p}=C_{m_p}\); all central and edge stabilizers are trivial. The fundamental-group theorem for graphs of groups with trivial edge groups yields
\[
\ker\rho\cong F_{(p-1)(q_p-1)}*\bigast_{j=1}^{q_p}C_{m_p},
\]
proving the stated fundamental-group formula.

**4. Integral homology.** Abelianizing that free product gives the asserted integral first homology. Because \(K_p\) is a connected two-dimensional simplicial complex, its second homology is a subgroup of its free abelian cellular two-chain group and is therefore free abelian. Since its Euler characteristic is \(p\), we obtain
\[
\operatorname{rank}H_2(K_p;\mathbb Z)=\chi(K_p)-1+\operatorname{rank}H_1(K_p;\mathbb Z)
=p-1+(p-1)(q_p-1)=q_p(p-1).
\]
There are no simplices of dimension greater than two, completing the proof.

## Verification
The standalone program `verification/check_ap.py` independently enumerates every vertex, edge and unordered progression triangle, constructs the oriented simplicial boundary matrix, computes its **integral Smith normal form**, and checks the predicted free ranks and torsion invariant factors. It checks all twelve primes \(p=5,7,11,13,17,19,23,29,31,37,41,43\), including mixed free-and-torsion examples. The recorded execution ends in `VERIFY_OK`; the computation is independent of the group-theoretic proof and is not an infinite-prime proof.

For instance, \(p=11\) gives \(\pi_1(K_{11})\cong C_3\), \(H_1\cong\mathbb Z/3\), and \(H_2\cong\mathbb Z^{10}\); \(p=41\) gives \(\pi_1(K_{41})\cong F_{40}*C_{25}*C_{25}\) and \(H_2\cong\mathbb Z^{80}\). These exemplify torsion and mixed behavior.

## Relationship to prior work
Ehrenborg, Govindaiah, Park and Readdy introduced the **linear, non-wrapping** van der Waerden progression-facet complex and studied its homotopy and contractibility [1]. Hooper and Van Tuyl studied its shellability and Cohen–Macaulay properties [2]. Earlier cyclic arithmetic-progression hypergraphs were studied in Ramsey theory [3], and Liber's later investigation addresses independence numbers and coloring bounds for these cyclic hypergraphs [4]. The complex here uses the same cyclic progression *hyperedges as facets*, but the calculation concerns its fundamental group and integral torsion. The result is neither a deduction from the linear non-wrapping complex's theorems nor from cyclic hypergraph independence numbers; the comparison does not establish exhaustive priority against differently indexed literature.

## Limitations
This theorem assumes prime modulus at least five, with precisely three distinct terms per progression. It does not treat composite moduli, longer progressions, the independence complex, higher homotopy groups, or determine a full homotopy equivalence beyond fundamental group and homology. The computational checks cover only the explicitly listed primes; the arbitrary-prime result follows from the proved quotient presentation and covering-kernel calculation. No independent audit has been performed.

## References
[1] R. Ehrenborg, L. Govindaiah, P. S. Park and M. Readdy, *The van der Waerden complex*, arXiv:1605.00663 (first public 2016-05-02), J. Number Theory 172 (2017), 287–300.

[2] B. Hooper and A. Van Tuyl, *A note on the van der Waerden complex*, arXiv:1707.07573 (2017).

[3] J. Burkert and P. Johnson, *Szlam's lemma: mutant offspring of a Euclidean Ramsey problem from 1973, with numerous applications*, in Ramsey Theory, Progress in Mathematics 285 (2011), 97–113.

[4] B. Liber, *On the Independence Numbers of the Cyclic Van der Waerden Hypergraphs*, arXiv:2509.07926 (2025).
