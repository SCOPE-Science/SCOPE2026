# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked at the level of each norm estimate and corner orientation.

The first key estimate is intrinsic to the predual. For B(omega)=d omega r and C(omega)=(1-d) omega (1-r), the adjoint of P=B+C is

P*(a)=r a d+(1-r)a(1-d)=(a+s_r a s_d)/2,

with s_r=1-2r and s_d=1-2d self-adjoint unitaries. Hence P is contractive. The two summands lie in orthogonal rectangular predual corners, so the cited corner-additivity lemma gives ||B omega||+||C omega||=||P omega||. Passing this estimate to the projective tensor norm is valid by taking finite representations and then completion.

The localization step uses only facts proved for arbitrary atomless von Neumann algebras in Huang--Nessipbayev--Sukochev--Xu: a top spectral projection of the slice functional, the small-corner Lemma 7.3 for finitely many normal functionals, and rectangular-corner duality. The element k need only approximately norm the corner rbd; norm attainment is not assumed. Choosing the approximation parameter rho with (1-rho)^2>1-alpha is sufficient to place k tensor y0 in the prescribed tensor slice.

For the witness map, the scalar functional H factors through the B-corner and therefore satisfies |H(z)| <= ||(B tensor I)z||. Consequently

Phi(z)=(C tensor I)z+H(z)z'

is contractive for every target z' in the unit ball. Since Bk=k and Ck=0, Phi(k tensor y0)=z' exactly. The finite set is almost fixed because d omega and omega r can be made arbitrarily small on every coefficient of an algebraic approximation; the errors pass to the original tensors using ||B||,||C||<=1. No trace, semifinite representation, centralizer, approximation property, or complementability assumption is used.

The converse characterization is also sound: taking Y=C reduces the tensor product to M_*, ODP implies the Daugavet property, and Oikhberg's theorem characterizes the Daugavet property of a von Neumann predual by non-atomicity of the algebra.

## Originality

The closest current source, Qi--Liu--Li, arXiv:2609.18044v1, explicitly assumes that M is diffuse semifinite with a faithful normal semifinite trace and proves ODP for L1(M,tau) tensor_pi Y. Its localization argument uses finite-trace spectral truncation and equal-trace partitions.

Huang--Nessipbayev--Sukochev--Xu, arXiv:2608.30491v1, prove that M_* has ODP for an arbitrary atomless, not necessarily semifinite, von Neumann algebra. Their theorem does not state the arbitrary-Y projective-tensor ODP conclusion, but their small rectangular-corner lemma supplies exactly the trace-free localization needed to make the semifinite tensor replacement argument work.

Searches using the exact source identifiers and combinations of "operator Daugavet property", "von Neumann predual", "projective tensor", "nonsemifinite", "type III", and synonymous formulations did not reveal an existing arbitrary-von-Neumann tensor theorem.

The main older tensor literature was checked for possible automatic implications. ODP is known as a sufficient device for Daugavet-type tensor conclusions, and WODP has tensor stability when both factors satisfy WODP; the available arbitrary-second-factor WODP theorem gives a weaker diametral diameter-two conclusion rather than ODP. Thus no generic tensor permanence result found in the inspected literature subsumes the present statement.

Residual prior-art risk remains: a very recent unindexed preprint or an older result phrased in terms of rectangular predual decompositions rather than ODP could contain an equivalent theorem. The originality judgment is therefore explicitly to the best of our knowledge.

## Value

The theorem removes the structural semifiniteness restriction from a result posted only days earlier and covers diffuse type III algebras. It also isolates a reusable principle: the trace partition in the semifinite tensor proof can be replaced by normal-functional small-corner localization, while the exact projective-norm contraction survives through rectangular L-summand geometry. The resulting witnesses are at least as strong as in the semifinite theorem: the slice point is elementary, every unit-ball target is reached exactly, and the interpolating maps are contractions.

## Limitations

The theorem is complex; no real version is claimed. It is special to von Neumann preduals and does not establish arbitrary-Y ODP permanence for general Banach spaces with ODP. It does not address completely bounded/operator-space tensor norms. No independent audit has been performed.
