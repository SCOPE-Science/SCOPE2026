# Short-word trace census of hyperbolic triangle groups over 2<=p<=q<=r<=6, with Euclidean-boundary contrast

## Context

Which short words in a hyperbolic triangle group are already hyperbolic, and at
what smallest displacement, is the concrete bounded form of the Fuchsian
trace-spectrum / systole question (Maskit trace identities, Singerman subgroup
geometry, McMullen length-spectrum programs). The natural classification
boundary is 1/p+1/q+1/r = 1 (spherical / Euclidean / hyperbolic). This record
gives the complete replayable short-word trace table over the smallest
nontrivial window exhibiting that threshold.

## Definitions

- Window: W_hyp = the 24 triples 2<=p<=q<=r<=6 with 1/p+1/q+1/r<1;
  W_eucl = {(3,3,3),(2,4,4),(2,3,6)} (all triples with sum = 1 in range).
- D(p,q,r) = <a,b | a^p = b^q = (ab)^r = 1> (von Dyck / orientation subgroup).
- Hyperbolic model (committed): A = Rot(2pi/p); B = M Rot(2pi/q) M^{-1} with
  M = diag(sqrt(mu),1/sqrt(mu)), mu+1/mu = 2t,
  t = (cos(pi/p)cos(pi/q)+cos(pi/r))/(sin(pi/p)sin(pi/q)) > 1.
  Then tr(A)=2cos(pi/p), tr(B)=2cos(pi/q), tr(AB)=-2cos(pi/r);
  A^p=B^q=(AB)^r=+-I in SL(2,R); discrete and faithful.
- Euclidean model (committed): affine maps a(z)=zeta_p z,
  b(z)=zeta_q(z-1)+1, classified by exact integer rotation exponents.
- Enumeration (committed): reduced words lengths 0..L, L=10, with inverse rule
  inv['a']='a' if p==2 else 'A', inv['b']='b' if q==2 else 'B'
  (order-2 generators self-inverse: forbid 'aa' when p==2, 'bb' when q==2;
  otherwise forbid inverse adjacency).
  Closed totals: 3070 per exactly-one-2 triple (1+3(2^10-1));
  118097 per p,q>=3 triple (1+2(3^10-1)).
- Classification: |tr|>2 hyperbolic with translation length
  l = 2 arccosh(|tr|/2); |tr|<2 elliptic; |tr|=2 with matrix +-I trivial
  (relator consequence), else nontrivial parabolic.

## Result (bounded census)

For every triple in W_hyp, with the above model and L=10:

1. No nontrivial parabolic occurs: every |tr|=2 word is +-I
   (e.g. 45 trivial for (2,4,5); 37 for (6,6,6)).
2. Every triple attains a hyperbolic word. The in-bound minimum |tr|,
   translation length, canonical lex-first witness, and gap to the
   second-best distinct |tr| are (sorted by min |tr|; full counts and top-10
   logs in artifacts/summary.json):

| triple | min |tr| | l_min | witness(len) | n_triv/n_ell/n_hyp | gap |
|---|---|---|---|---|---|
| (2,4,5) | 2.288245611271 | 1.061275061905 | BBBBBBBab (9) | 45/1353/1672 | 0.329788 |
| (3,3,4) | 1+sqrt(2)=2.414213562373 | 1.265948638402 | AAAAAAAAB (9) | 1201/38332/78564 | 1.000000 |
| (2,4,6) | sqrt(6)=2.449489742783 | 1.316957896925 | BBBBBBBab (9) | 41/1117/1912 | 0.378937 |
| (2,5,5) | 3/2+sqrt(5)/2=2.618033988750 | 1.534394436503 | BBBBBBBBa (9) | 15/851/2204 | 0.618034 |
| (3,3,5) | 3/2+sqrt(5)/2 | 1.534394436503 | AAAAAAAAB (9) | 1017/31256/85824 | 0.618034 |
| (3,3,6) | 1+sqrt(3)=2.732050807569 | 1.662885891059 | AAAAAAAAB (9) | 1013/29716/87368 | 1.000000 |
| (2,5,6) | 2.802517076888 | 1.736596079923 | BBBBBBBBa (9) | 11/697/2362 | 0.433551 |
| (3,4,4) | 2sqrt(2)=2.828427124746 | 1.762747174039 | AAAAAAAAB (9) | 635/20480/96982 | 0.171573 |
| (2,6,6) | 3 | 1.924847300238 | BBBBBBBBa (9) | 9/545/2516 | 0.464102 |
| (3,4,5) | 3.032247551123 | 1.953415665111 | AAAAAAAAB (9) | 559/17516/100022 | 0.255998 |
| (3,4,6) | 3.146264369942 | 2.050306722504 | AAAAAAAAB (9) | 555/16984/100558 | 0.303225 |
| (3,5,5) | 1+sqrt(5)=3.236067977500 | 2.122550123810 | AAAAAAAAB (9) | 331/13010/104756 | 0.381966 |
| (3,5,6) | 3.350084796319 | 2.209739150704 | AAAAAAAAB (9) | 327/12636/105134 | 0.452432 |
| (4,4,4) | 2+sqrt(2)=3.414213562373 | 2.256767929933 | AAAAAAAAAb (10) | 349/11076/106672 | 1.414214 |
| (3,6,6) | 2sqrt(3)=3.464101615138 | 2.292431669561 | AAAAAAAAB (9) | 265/10796/107036 | 0.535898 |
| (4,4,5) | 5/2+sqrt(5)/2=3.618033988750 | 2.397827515308 | AAAAAAAAAb (10) | 301/9980/107816 | 0.084425 |
| (4,4,6) | 2+sqrt(3)=3.732050807569 | 2.471802046651 | AAAAAAAAAb (10) | 297/9872/107928 | 0.131652 |
| (4,5,5) | 3.906279600021 | 2.578940712713 | AAAAAAAAAb (10) | 161/6760/111176 | 0.125968 |
| (4,5,6) | 4.020296418840 | 2.645594497237 | AAAAAAAAAb (10) | 157/6650/111290 | 0.047227 |
| (4,6,6) | 4.181540550352 | 2.735693405967 | AAAAAAAAAb (10) | 159/5522/112416 | 0.232673 |
| (5,5,5) | 2+sqrt(5)=4.236067977500 | 2.765142618158 | AAAAAAAAAB (10) | 85/4548/113464 | 1.000000 |
| (5,5,6) | 4.350084796319 | 2.825177591358 | AAAAAAAAAB (10) | 81/4436/113580 | 0.070466 |
| (5,6,6) | 4.534567884457 | 2.918217984219 | AAAAAAAAAB (10) | 39/3532/114526 | 0.083466 |
| (6,6,6) | 3+sqrt(3)=4.732050807569 | 3.012744159639 | AAAAAAAAB (9) | 37/2900/115160 | 1.732051 |

   All second-best gaps are >= 0.047, so each minimum is well separated.
   Extremes: smallest minimum (2,4,5): |tr|=2.288245611271, l=1.061275061905;
   largest (6,6,6): |tr|=3+sqrt(3), l=3.012744159639.
   14 of 24 minima identify as a+b sqrt(d) as shown; the other 10 are
   certified numerically with closed forms left open.

3. Euclidean contrast: for every triple in W_eucl, zero hyperbolic words occur
   to L=10: (3,3,3): 118097 words: 1969 trivial / 78892 rotations / 37236
   translations; (2,4,4): 3070: 69/2277/724; (2,3,6): 3070: 59/2567/444.

## Proof / evidence

Computation, not analytic proof of a general theorem; the bounded census is
certified by two independent routes:

- Primary (census.py): float64 2x2 products over the deterministic reduced word
  tree; traces via numpy; classification tolerance 1e-9, triviality by
  allclose to +-I at 1e-8. Margins: smallest min|tr|-2 = 0.288 ((2,4,5));
  tolerance/margin ratio ~3.5e-9, so no boundary sensitivity.
- Independent replay (replay_verify.py): mpmath at 80 digits, different code
  path (recursive enumeration, adjugate inverses, +-I test at 1e-60);
  reproduces every triple's total, trivial/elliptic/hyperbolic counts, zero
  parabolics, and every minimum |tr| to <4e-13; generator identities
  tr(A),tr(B),tr(AB) hold to 1e-70. Euclidean replay uses exact integer
  rotation exponents with zero hyperbolic.
- Auditor recomputation from scratch (independent numpy + integer-exponent
  Euclidean code) reproduced 27/27 totals, all type counts, zero nontrivial
  parabolics, all 24 minima to <1e-9, and all gap values.
- Relator check: A^p=B^q=(AB)^r=+-I and t>1 verified for all 24 hyperbolic
  triples; 14/14 claimed radical exact forms verified to <1e-12.

## Limitations

- Minimum claimed only within len<=10 in the committed model; nothing about
  global systoles or minimal translation lengths of the groups.
- Model dependence stated explicitly (two-rotation Fuchsian embedding).
- 10 of 24 minima lack closed radicals; float values certified by two routes.
- Single traces are classical consequences of standard embeddings; the new
  content is the uniform bounded-minimum census with ranked word logs and
  Euclidean contrast.
- Witness canonicity is lex-first among ties (ties numerous, e.g. 24088
  minimizers for (3,3,4)); the min|tr| value is the invariant, the word is a
  representative.
- The window 2<=p<=q<=r<=6 does not contain (2,3,7), cited only as prior
  single-group literature.

## Reproducibility

- python3 output/artifacts/census.py — primary table
  (totals 3070 / 118097).
- python3 output/artifacts/replay_verify.py — independent 80-digit replay;
  expect REPLAY: ALL_OK (24/24 totals+counts, all minima).
- Reduced-word rule: inv['a']='a' if p==2 else 'A',
  inv['b']='b' if q==2 else 'B'; L=10.
- Machine-readable data: output/artifacts/summary.json (per-triple counts,
  minima, top-10 word logs, Euclidean logs), output/artifacts/table.csv
  (ranked minima table).

## References

- Moreno-Stypa, On the vertex-to-edge duality between the Cayley graph and
  the coset geometry of von Dyck groups, arXiv:1303.0962.
- Zimmermann, Large finite group actions on surfaces: Hurwitz groups, maximal
  reducible and handlebody groups, arXiv:2110.11050.
- Singerman, Subgroups of Fuchsian groups and finite permutation groups,
  BLMS 2.3.319 (1970).
- Schein-Shoan, Systolic length of triangular modular curves,
  arXiv:2012.08796.
- Karrer-Schwer-Struyve, The triangle groups (2,4,5) and (2,5,5) are not
  systolic, arXiv:1812.08567.
