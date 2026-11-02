# Independent mathematical audit

## correctness

PASS

For G_q=K_q□K_q with q>=2, L=q(Q⊗I+I⊗Q) and two-stage Radau IIA completed-step multiplier r(z)=(6-2z)/(z²+4z+6). Its tensor spectral decomposition yields exactly three entry types over positive E(x)=(x²+4x+6)(2x²+4x+3), x=qh: diagonal numerator D_q(x), adjacent numerator xF_q(x), and nonadjacent numerator 2x²(x²+9x+9). For q=2,3, D>0; for every q>=4 Descartes sign changes and D(0)>0>D(q), D(∞)>0 imply exactly two distinct positive roots a_q<b_q. The algebraic identity F=2x(x²+9x+9)+q(2x+3)(6-x) proves F>0 when x<=6 or x>=q; when 6<x<q, D(6)<0 and D(q)<0 imply the diagonal is already negative. Thus the full positivity set is [0,a_q/q]∪[b_q/q,∞), not just sampled intervals. Scalar |r|<=1 and the zero mode imply operator norm 1 at all h. Polynomial scaling gives a_q→3/2 and b_q/q²→1. Fresh independent SymPy inverse of the actual q=4 rook Laplacian at h=1 confirmed each diagonal -4/323 and row sums 1, with positive roots approximately 3.3633 and 14.2443 in x; these finite checks corroborate the symbolic proof. Stage positivity or rectangular rooks are not asserted.

## originality

PASS

Ketcheson's Numipedia gives the classical Radau IIA tableau and stability rational function, not the rook-graph positivity set. Gottlieb–Shu–Tadmor 2001 studies general strong stability preserving RK barriers, not the completed step on a specific tensor Laplacian. Blanes–Iserles–Macnamara 2021/22 discusses positivity-preserving ODE and graph-Laplacian schemes and general barriers, but not this explicitly parameterized Radau rook graph. Its publicly accessible PDF text was inspected; screenshot retrieval was blocked so no claim of visually checked PDF pages. Resultary query returned different methods (SSP-SDIRK2, Gauss Padé) or unrelated rook homology, not the same method/graph statement. Distinct time-step positivity and spectral stability demand different sign conditions. Provisional PASS with historical-specialization priority risk.

## value

PASS

This is a complete infinite-family positivity-domain classification for a standard third-order stiff integrator on a natural highly symmetric graph. The disconnected reentrant positivity set is counterintuitive: tiny and sufficiently large steps are positive, intermediate ones create negative state entries even though the step is spectrally nonexpansive and conservative. The q=4 threshold and scaling 3/(2q) versus q give practically meaningful separation and a nontrivial method/graph phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
