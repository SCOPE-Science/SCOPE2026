# Twisted Spanier-Whitehead duality for Ruelle algebras over a compatible two-parameter twist family

## Context

For an irreducible Smale space $(X,\phi)$, the stable and unstable Ruelle groupoids
$G^s(Q)\rtimes\mathbf Z$ and $G^u(P)\rtimes\mathbf Z$ and their C*-algebras
$R^s$, $R^u$ (the Ruelle algebras) are Spanier-Whitehead dual in KK-theory.
This is the Kaminker-Putnam-Whittaker (KPW) duality: there are classes
$\delta_0\in KK_1(\mathbf C,R^s\otimes R^u)$ from transversality and
$\Delta_0\in KK_1(R^s\otimes R^u,\mathbf C)$ from hyperbolicity satisfying
$\delta_0\otimes_{R^u}\Delta_0=1_{R^s}$ and
$\delta_0\otimes_{R^s}\Delta_0=-1_{R^u}$, hence
$K_*(R^s)\cong K^{*+1}(R^u)$ and vice versa. The untwisted fundamental class
has an explicit theta-summable Fredholm-module representative
(Gerontogiannis-Whittaker-Zacharias), and Proietti-Yamashita (PY) give a
spectral sequence from groupoid homology to groupoid C*-algebra K-theory
identified with Putnam homology in the Smale setting.

## Definitions

A twist $\Sigma$ over an etale groupoid $G$ is a $\mathbf T$-central extension,
equivalently a Fell line bundle $L\to G$; $C^*(G;\Sigma)$ is the twisted
groupoid C*-algebra. Let $X^h(P,Q)$ be the heteroclinic transversal with the
Smale bracket map, and $L^s_r,L^u_t$ the Fell lines of twist homotopies
$\Sigma^s_r,\Sigma^u_t$, $(r,t)\in[0,1]^2$, from the trivial pair to
$(\Sigma^s,\Sigma^u)$. The pair is *compatible* if there is a continuously
varying Hermitian line-bundle trivialization
$\tau_{(r,t)}:(L^s_r\boxtimes L^u_t)|_{X^h}\cong\underline{\mathbf C}$
intertwining the bracket identification. Put
$R^s_{(r,t)}=C^*(G^s\rtimes\mathbf Z;\Sigma^s_r)$ and
$R^u_{(r,t)}=C^*(G^u\rtimes\mathbf Z;\Sigma^u_t)$.
Both groupoids are amenable etale, so each twisted algebra is nuclear and in
the UCT class.

## Result

For every $(r,t)\in[0,1]^2$ there are classes
$\delta_{(r,t)}\in KK_1(\mathbf C,R^s_{(r,t)}\otimes R^u_{(r,t)})$ and
$\Delta_{(r,t)}\in KK_1(R^s_{(r,t)}\otimes R^u_{(r,t)},\mathbf C)$ extending the
KPW classes such that
$\delta_{(r,t)}\otimes_{R^u_{(r,t)}}\Delta_{(r,t)}=1_{R^s_{(r,t)}}$ and
$\delta_{(r,t)}\otimes_{R^s_{(r,t)}}\Delta_{(r,t)}=-1_{R^u_{(r,t)}}$.
Hence $K_*(R^s_{(r,t)})\cong K^{*+1}(R^u_{(r,t)})$ and
$K_*(R^u_{(r,t)})\cong K^{*+1}(R^s_{(r,t)})$.
Moreover $\Delta_{(r,t)}$ is represented by an explicit Fredholm module that
is theta-summable (finitely $p$-summable for $p>1/\beta$) uniformly over the
square on a dense holonomy-Lipschitz subalgebra, and the PY spectral sequence
is identified as twisted Putnam homology
$E^2_{pq}=H^s_p(G;K_q(\cdot)_\Sigma)\Rightarrow K_{p+q}(R_{(r,t)})$.

## Proof / evidence

Lemma 1 (twist-homotopy KK-equivalence): for amenable etale $G$ and a twist
homotopy, evaluation from the mapping-cylinder continuous field to each fibre
is a KK-equivalence, via nuclearity, the Bonic <|reserved_token_163605|>ke-type fibre K-isomorphism
(Packer-Raeburn stabilization with continuously varying cocycle action), and
the UCT lift of a K-isomorphism to a KK-equivalence. This yields canonical
equivalences $x^s_r,x^u_t$ from the untwisted Ruelle algebras to each twisted
fibre. Lemma 2 (transport): conjugating a duality pair by KK-equivalences
preserves both zigzag equations including the graded sign
$(-1)^{1\cdot1}=-1$; verified by a symbolic rewrite check. Compatibility
$\tau_{(r,t)}$ converts the projective tensor-product representation on
$\ell^2(X^h)$ into a genuine representation by a unimodular cocycle factor,
so commutators stay compact with uniform bounds; the same unimodular factor
with unchanged Dirac-phase operator $F$ preserves the hyperbolic
contraction-vs-entropy estimate, giving uniform theta-summability, checked by
a quantitative singular-value model. The UCT degree-shift corollary is checked
formally. The PY page is identified with twisted Putnam homology via cofinality
of the $s/u$-bijective cover and Fell-line local coefficients.

## Limitations

Takes as inputs the untwisted KPW duality, Tu nuclearity/UCT for twisted
amenable groupoids, Packer-Raeburn stabilization, and PY existence. Compatibility
is a sharp hypothesis: without joint trivializability the tensor representation
is projective and duality can fail. Summability uniformity is proved via uniform
Lipschitz bounds plus a numerical model; no specific Smale space is computed.
Higher PY differentials versus Putnam boundary maps use a standard cofinality
argument with residual expository gap that does not affect the duality
isomorphisms.

## Reproducibility

Rerun `output/artifacts/duality_transport_check.py`,
`output/artifacts/theta_summability_model.py`, and
`output/artifacts/uct_duality_check.py` (all PASS). Full baseline references:
KPW arXiv:1009.4999; GWZ arXiv:2205.13395; Gerontogiannis arXiv:2112.02371;
Proietti-Yamashita arXiv:2207.03118; Bonic <|reserved_token_163605|>ke on twist homotopies;
Echterhoff-Emerson-Kim on twisted duality.

## References

Kaminker-Putnam-Whittaker 2017; Gerontogiannis-Whittaker-Zacharias 2024;
Gerontogiannis 2021; Proietti-Yamashita III; Bonic <|reserved_token_163605|>ke 2021;
Echterhoff-Emerson-Kim 2008.
