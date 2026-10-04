# Finite entropy forces an abelian stable image for shadowing compact-group endomorphisms
## Finding
Let \(G\) be a compact connected Hausdorff group and let \(\alpha:G\to G\) be a continuous endomorphism with the shadowing property. Define the stable image by
\[
K=\bigcap_{n\ge 0}\alpha^n(G).
\]
If \(K\) is nonabelian, then
\[
h_{\mathrm{top}}(\alpha)=\infty.
\]
Equivalently, if \(h_{\mathrm{top}}(\alpha)<\infty\), then \(K\) is abelian. For a surjective endomorphism, \(K=G\), so every surjective shadowing endomorphism of a compact connected nonabelian group has infinite topological entropy.

## Assumptions and scope
Topological entropy is the usual Adler--Konheim--McAndrew entropy on compact Hausdorff systems; on compact metrizable factors it agrees with the standard separated-set definition. No metrizability or Lie hypothesis is imposed on \(G\). The conclusion concerns the stable image, which is the natural surjective core of an arbitrary endomorphism.

The input from Peng is the 2026 structural characterization of shadowing endomorphisms of compact connected groups. For \(K\) as above, write \(\beta=\alpha|_K\), set \(S=K'\), and use the decomposition
\[
S/Z(S)\cong\prod_{i\in I} S_i,
\]
where each \(S_i\) is a center-free simple connected compact Lie group. Shadowing forces the induced injective map \(\tau:I\to I\) to have no periodic point, and every component of its functional graph becomes a one-sided or two-sided full shift after coordinate identifications.

## Proof
Peng's stable-image reduction gives that \(K\) is compact and connected, \(\beta:K\to K\) is surjective, and \(\beta\) has shadowing whenever \(\alpha\) does. Suppose that \(K\) is nonabelian. Then \(S=K'\) is nontrivial. Since \(S\) is connected semisimple, the product \(S/Z(S)\cong\prod_{i\in I}S_i\) has at least one simple factor.

Peng's semisimple criterion says that shadowing of \(\beta\) forces \(\tau\) to have no periodic point. Choose one component \(J\subseteq I\). The coordinate projection
\[
S/Z(S)\longrightarrow\prod_{i\in J}S_i
\]
is an equivariant factor map. By Peng's coordinate straightening, the induced system on this component is topologically conjugate either to the one-sided full shift \(\sigma_+:H^{\mathbb N}\to H^{\mathbb N}\) or to the two-sided full shift \(\sigma:H^{\mathbb Z}\to H^{\mathbb Z}\), for a nontrivial simple connected compact Lie group \(H\).

Either full shift has infinite topological entropy. Indeed, fix an integer \(m\ge2\) and choose \(m\) distinct points of \(H\). Because this finite set has positive minimum pairwise distance, words of length \(n\) in these \(m\) symbols, extended by a fixed symbol outside the first \(n\) coordinates, form an \(n,\varepsilon_m\)-separated set of cardinality \(m^n\) for some \(\varepsilon_m>0\). Hence the shift entropy is at least \(\log m\). Since \(m\) is arbitrary, the entropy is infinite.

Topological entropy does not increase under factors and does not exceed the entropy of an ambient system when restricted to a closed invariant subsystem. Thus
\[
h_{\mathrm{top}}(\alpha)\ge h_{\mathrm{top}}(\beta)\ge h_{\mathrm{top}}(\beta|_S)\ge h_{\mathrm{top}}(\overline{\beta}|_J)=\infty,
\]
where \(\overline{\beta}\) denotes the induced endomorphism on \(S/Z(S)\). Therefore \(h_{\mathrm{top}}(\alpha)=\infty\).

## Verification
The proof uses only the stable-image and semisimple-factor statements explicitly proved in arXiv:2608.00955v1, plus standard entropy monotonicity and the displayed separated-set argument for a full shift. The full-shift argument is independent of any finite-dimensional entropy formula and works because each simple compact Lie alphabet is nontrivial and therefore contains finite subsets of arbitrarily large cardinality.

The boundary cases behave as expected. If \(K\) is abelian, the theorem makes no claim that entropy is finite; abelian shift-type directions can still produce infinite entropy. Conversely, hyperbolic toral automorphisms give familiar finite-entropy shadowing examples with abelian stable image. Thus the conclusion isolates the nonabelian stable component rather than asserting an equivalence between abelianness and finite entropy.

## Relationship to prior work
Peng's arXiv:2608.00955v1, first posted 2026-08-02, has primary MSC 37B65 and gives the decisive shadowing classification. Its Remark 5.10 identifies the center-free semisimple quotient, under the shadowing condition, with a product of one-sided and two-sided full shifts on simple connected compact Lie groups. The paper does not state an entropy consequence.

Caldas and Patrão, arXiv:1105.4344v2 and the corresponding 2013 DCDS article, prove in the finite-dimensional Lie-group setting that a surjective endomorphism of a compact semisimple Lie group has zero entropy. There is no conflict: Peng's criterion rules out shadowing for such a nontrivial finite semisimple factor, because a finite permutation of simple factors necessarily has a periodic orbit. The present result concerns the genuinely infinite-factor situation allowed for general compact connected groups, where shadowing forces full-shift components and hence infinite entropy.

Searches of a published-finding database and the public literature for finite-entropy shadowing compact connected group endomorphisms, stable-image abelianness, and semisimple full-shift entropy did not locate a theorem implying this stable-image obstruction. Those negative searches support, but do not by themselves establish, originality.

## Limitations
The result does not classify entropy on the abelian stable part, does not claim a converse, and does not quantify entropy below infinity. It depends on Peng's structural theorem for shadowing endomorphisms; it is not an independent reproof of that classification. Literature searches cannot exclude every differently phrased prior corollary, so the originality assessment is limited to the inspected sources and implication comparisons.

## References
1. D. Peng, *Shadowing Endomorphisms of Compact Groups*, arXiv:2608.00955v1, 2026.
2. A. Caldas and M. Patrão, *Entropy of Endomorphisms of Lie Groups*, arXiv:1105.4344v2; Discrete Contin. Dyn. Syst. 33 (2013), 1351--1363, DOI:10.3934/dcds.2013.33.1351.
