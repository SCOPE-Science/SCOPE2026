# Every carrier size at least four realizes the pentagon with two-valued unary operations

## Finding
Let \(N_5\) denote the five-element nondistributive pentagon lattice, with elements \(0<\rho<\sigma<1\) and \(0<\tau<1\), where \(\tau\) is incomparable with \(\rho\) and \(\sigma\). For a finite lattice \(L\), let \(\operatorname{spec}_2(L)\) be the set of cardinalities of finite carrier sets admitting a unary algebra whose basic operations all have **exactly two** values and whose congruence lattice is isomorphic to \(L\). Then
\[
\boxed{\operatorname{spec}_2(N_5)=\{4,5,6,\ldots\}.}
\]
In particular, for every integer \(n\ge4\), there is an explicit finite family of exactly two-valued unary operations on an \(n\)-element set whose congruence lattice has exactly five elements and is \(N_5\). Together with the already established spectra for distributive lattices and the five-element diamond \(M_3\), this completes the size spectrum of every lattice having at most five elements.

## Assumptions and scope
A unary algebra means a set equipped with any finite family of unary maps. Every map in the construction must have image of cardinality exactly \(2\); constant maps are not used. A congruence is an equivalence relation invariant under every basic map. The lattice \(N_5\) is ordered by inclusion of equivalence relations, and the spectrum records carrier cardinalities, not the number of maps. The theorem is for finite carriers only.

## Proof
Fix an integer \(r\ge2\), and set
\[
B=\{1,\ldots,r\},\qquad A=B\mathbin{\dot\cup}\{x,y\}.
\]
Define three equivalence relations on \(A\): \(\rho\) has exactly one nonsingleton block \(B\); \(\sigma\) has the two blocks \(B\) and \(\{x,y\}\); and \(\tau\) has exactly two nonsingleton blocks \(\{1,x\}\) and \(\{2,y\}\). Along with the equality and universal relations \(0_A,1_A\), they form a five-element pentagon: \(0_A<\rho<\sigma<1_A\), while \(\tau\) is incomparable with \(\rho\) and \(\sigma\), meets both in \(0_A\), and joins both to \(1_A\).

For **every** map \(g:B\to B\) having exactly two values, define its extension \(\widehat g:A\to A\) by
\[
\widehat g(b)=g(b)\ (b\in B),\qquad \widehat g(x)=g(1),\qquad \widehat g(y)=g(2).
\]
Add the two maps \(h_x,h_y:A\to A\) defined by
\[
h_x(b)=x\ (b\in B),\quad h_x(x)=h_x(y)=1;
\qquad
h_y(b)=y\ (b\in B),\quad h_y(x)=h_y(y)=2.
\]
Each extension \(\widehat g\) still has exactly two values, as do \(h_x\) and \(h_y\). Let \(\mathcal F\) be this finite family; it has
\[
\binom r2(2^r-2)+2
\]
distinct maps (choose the two output values and a nonconstant binary assignment on \(B\)).

All five listed relations are invariant under every map in \(\mathcal F\). For \(\widehat g\), the block \(B\) maps into \(B\), and the pairs \(\{1,x\}\) and \(\{2,y\}\) have equal images. For \(h_x\), the whole block \(B\) maps to \(x\), the pair \(\{x,y\}\) maps to \(1\), and each of the two pairs of \(\tau\) maps into \(\{1,x\}\); the analogous statement for \(h_y\) uses \(\{2,y\}\). Thus \(0_A,\rho,\sigma,\tau,1_A\) are congruences.

Conversely, let \(\theta\) be any congruence of \((A;\mathcal F)\). Its restriction to \(B\) is preserved by **every** two-valued map \(g:B\to B\). If it identifies distinct elements \(b,b'\in B\), then for arbitrary distinct \(u,v\in B\) choose \(g\) with \(g(b)=u\) and \(g(b')=v\). Hence \(u\mathrel\theta v\). It follows that \(\theta|_B\) is either equality or the universal relation on \(B\).

Suppose first that \(\theta|_B\) is equality. If \(x\mathrel\theta b\) for some \(b\in B\), then \(g(1)=\widehat g(x)\mathrel\theta\widehat g(b)=g(b)\) for every two-valued \(g\). Since distinct points of \(B\) cannot be equivalent, \(b=1\): if \(b\ne1\) we can choose \(g(1)\ne g(b)\). Similarly \(y\) can be equivalent to a point of \(B\) only to \(2\). Also \(x\not\mathrel\theta y\), since choosing \(g(1)\ne g(2)\) would identify distinct points of \(B\). Finally, if \(x\mathrel\theta1\), applying \(h_y\) yields \(2=h_y(x)\mathrel\theta h_y(1)=y\); conversely, \(y\mathrel\theta2\) and \(h_x\) yield \(1\mathrel\theta x\). Therefore \(\theta=0_A\) or \(\theta=\tau\).

Suppose next that \(\theta|_B\) is universal, so \(\rho\le\theta\). If any point of \(B\) is \(\theta\)-equivalent to \(x\), applying \(h_y\) identifies \(y\) with a point of \(B\); then all three blocks \(B,\{x\},\{y\}\) coalesce and \(\theta=1_A\). Similarly, if a point of \(B\) is equivalent to \(y\), applying \(h_x\) forces \(\theta=1_A\). Otherwise the only possible extra identification is \(x\mathrel\theta y\), yielding \(\theta=\rho\) or \(\theta=\sigma\). Thus the entire congruence lattice is precisely \(\{0_A,\rho,\sigma,\tau,1_A\}\cong N_5\), on \(r+2\) points.

For the converse bound, any congruence lattice on an \(n\)-element carrier is a sublattice of the partition lattice \(\operatorname{Eq}(A)\), whose maximal strict chain length is \(n-1\). Since \(N_5\) has a strict chain of length \(3\), it requires \(n\ge4\), even without any bound on operation ranges. Taking \(r=n-2\) in the explicit construction realizes all \(n\ge4\) and proves the theorem.

## Verification
The companion standalone `verify.py` constructs exactly the maps in the proof for \(r=2,3,4,5,6\) and enumerates every equivalence relation of the corresponding carriers (orders \(4\) through \(8\)). It tests the congruence condition directly for every relation and every map. In every case the surviving relations are exactly \(0_A,\rho,\sigma,\tau,1_A\). The script also checks the number of distinct operations and verifies that each has image cardinality \(2\). Running `python3 verify.py` yields the embedded `verification_output.txt`, ending in `VERIFY_OK`. This finite verification corroborates examples; the preceding argument proves the unbounded statement.

## Relationship to prior work
Dormán, Kátai-Urbán, Horváth and Waldhauser (2026, arXiv:2610.33305v1) introduce \(\operatorname{spec}_2\) in Problem 40. Their Proposition 41 identifies the five-element diamond spectrum \(\operatorname{spec}_2(M_3)=\{3\}\), because \(M_3\cong\operatorname{Eq}([3])\). Their Proposition 42 determines the spectrum of every nontrivial distributive finite lattice as the upper ray beginning at one more than its height. Appendix B provides one four-point representation of the pentagon, establishing the minimum carrier size, but does not give this complete unrestricted cardinality spectrum. The present uniform two-valued construction supplies all larger cardinalities for the remaining five-element nondistributive lattice. The earlier general characterization by Bandelt (1977) is acknowledged as a possible antecedent for the technique, but the exact pentagon spectrum is not explicitly stated in the checked recent paper.

## Limitations
The result does not determine \(\operatorname{spec}_2(L)\) for arbitrary nondistributive lattices, classify minimal numbers of operations, or classify all realizations of \(N_5\). The construction uses a potentially large family of maps; minimal map counts were not claimed. Historical completeness of priority, especially in Bandelt's 1977 treatment of two-valued congruence lattices and older unary-algebra literature, has not been independently established.

## References
1. M. Dormán, K. Kátai-Urbán, E. K. Horváth, T. Waldhauser, *Congruence lattices of 2-valued unary algebras*, arXiv:2610.33305v1 (first submitted 23 October 2026), https://arxiv.org/html/2610.33305v1. Relevant material: Problem 40, Propositions 41–42, Appendix B §B.3.
2. H.-J. Bandelt, *On congruence lattices of 2-valued algebras*, in *Contributions to Universal Algebra*, Colloq. Math. Soc. János Bolyai 17 (1977), 27–31. Earlier general characterization; full chapter not inspected.
