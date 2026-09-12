# Minimal pair in the degree spectrum of a finite-Ulm-length p-group

## Context

Fix a prime p. For a countable structure G with universe omega, the degree
spectrum DgSp(G) is the set of Turing degrees of (atomic diagrams of)
structures with universe omega isomorphic to G, computable or not. A minimal
pair of Turing degrees is a pair a,b > 0 with a wedge b = 0, i.e. two
nonzero degrees with no nonzero degree below both. The Jockusch-Soare theorem
states that such a minimal pair exists among the c.e. degrees. The admitted
target asks: does there exist a computable reduced abelian p-group G of finite
Ulm length n >= 1, universe omega, specified Ulm invariants, divisible part
zero, whose degree spectrum contains a minimal pair, either by constructing
such G or by proving no such G exists.

Note on wording: the topic statement writes DgSp(G) using a clause rendered
as "X computable in X". Read literally over computable copies only, every
spectrum would be {0} and the question vacuous. The target plainly intends
the standard definition above (it asks for copies of degrees a,b > 0 and
suggests a permitting construction). This audit uses the standard definition.

## Definitions

- H = Z/p^2 (+) Z/p. G = H^{(omega)}, the countable direct sum of copies of H.
- Ulm subgroups: G_0 = G, G_{alpha+1} = p G_alpha, G_lambda = intersection for
  limit lambda. Length is the least lambda with stabilization; G is reduced if
  its maximal divisible subgroup is 0.
- Ulm invariants f_alpha(G) = dim_{F_p} P_alpha/P_{alpha+1} where
  P_alpha = {x in G_alpha : p x = 0}.
- P(A) = pA = {x : exists y (p y = x)}, c.e. in any copy uniformly.
- Coding block B = H (+) H = <a>(+) <b> (+) <c> (+) <d> with
  ord(a)=ord(c)=p^2, ord(b)=ord(d)=p, of order p^6. Witness atoms
  t* = b, s* = p c, both nonzero socle elements.
- Layout B^0: standard table +_S. Layout B^1: transport of +_S along the
  single transposition pi swapping t* <-> s* (fixing 0 and all else),
  x (+) y := pi(pi(x)+pi(y)).
- Universe encoding: N = p^6, each block identified with Z_N, every
  n in omega written uniquely in base N with finite support,
  n = SUM_i d_i(n) N^i. Witnesses tau_i = t* N^i, sigma_i = s* N^i.
  Addition is componentwise per block layout L_i in {S,T}.
- For a c.e. set C with enumeration (C_s), A_C is the group on omega with
  L_i = S if i not in C and L_i = T if i in C (each block switches at most
  once).

## Result

For every prime p, the computable reduced abelian p-group
G = (Z/p^2)^{(omega)} (+) (Z/p)^{(omega)} has Ulm length exactly 2,
divisible part 0, Ulm invariants f_0 = f_1 = aleph_0 (all higher 0),
universe omega, and its degree spectrum contains a minimal pair. In fact
every c.e. degree lies in DgSp(G): for every c.e. C, the copy A_C defined
above satisfies A_C ~= G and deg(A_C) = deg(C). Applying this to the
Jockusch-Soare noncomputable c.e. minimal pair C,D gives copies
A_C, A_D ~= G of degrees a,b > 0 with a wedge b = 0.

## Proof / evidence

Lemma (invariants). p^2 G = 0 so G^2 = 0 and length <= 2; pG != 0 so length
exactly 2. A bounded p-group has trivial divisible part, so G is reduced.
Each Z/p^2 summand contributes one dimension to each of f_0,f_1 and each Z/p
summand one to f_0; infinitely many of each give f_0 = f_1 = aleph_0 by
Pruefer's theorem for bounded groups.

Block pair. In the standard layout, s* = p c is p-divisible (witness c)
while t* = b is not: every p-multiple p(x,y,z,w) = (px,0,pz,0) has zero
Z/p-coordinates. For the transport, pth-powers correspond via
p_(+) v = pi(p_(+) pi(v)), hence w is (+)-divisible iff pi(w) is
(+)-divisible (identity (1)); with pi swapping t*,s* the pattern is exactly
swapped: in B^1, t* is p-divisible and s* is not, and B^1 ~= B^0 ~= H (+) H.
No pre-swap and no automorphism of the standard block is asserted.

Purity. If z supported only in block i equals p w in A_C, the coordinate
projection pr_i (a homomorphism onto block i) gives z = p w_i inside block i;
conversely block-i divisibility lifts via single-support witnesses. Hence
(*) tau_i in p A_C iff i in C, sigma_i in p A_C iff i not in C.

Type preservation. Every block is ~= H (+) H in both layouts, so
A_C ~= H^{(omega)} ~= G for every c.e. C, uniformly in p and c.e. index.

Degrees. (a) C <=_T A_C: C = {i : tau_i in P(A_C)} and complement C =
{i : sigma_i in P(A_C)}, both c.e. in A_C, so by relativized Post,
C <=_T A_C; concretely dovetail-search p y = tau_i vs p y = sigma_i, exactly
one of which terminates by (*). (b) A_C <=_T C: with a C oracle each block's
final layout is decided by one query; to compute m +_{A_C} n decode digits,
read finite support, query C on it, look up finite tables, re-encode. Hence
deg(A_C) = deg(C).

Minimal pair. Jockusch-Soare (black box) gives noncomputable c.e. C,D with
a wedge b = 0; A_C, A_D are the intended copies. Length 1
(F_p-vector space) is computably categorical among computable copies, so this
socle-vs-pth-powers coding needs length at least 2; n = 2 is least for this
method (no claim that the full noncomputable-copy spectrum of length 1 is
{0}). The construction is injury-free (independent blocks, at most one action
each), discharging the target's priority-permitting option degenerately.

Computational evidence. output/artifacts/check_blocks.py (pure stdlib,
deterministic) verifies for p = 2,3,5: group axioms for layouts S (=B^0) and
T (=B^1), complementary witness patterns, socle p^4, |pB| = p^2, truncation
counts. The general-prime case is the uniform proof above.

## Limitations

- The Jockusch-Soare minimal-pair theorem is cited as a black box.
- The script verifies block micro-claims only for p = 2,3,5; the general prime
  rests on the uniform transport identity.
- Only c.e. degrees are coded; the full spectrum of G is not characterized.
- The length-1 remark concerns computable categoricity among computable
  copies, not the full spectrum.

## Reproducibility

Run `python3 output/artifacts/check_blocks.py` (no dependencies); expect
ALL BLOCK CHECKS PASSED. Re-derive general p from Section Proof above:
coordinate check for B^0 plus identity (1) for B^1, purity by projection,
degree equalities by Post/dovetail and C-oracle table evaluation.

## References

- W. Calvert, D. Cenzer, V. Harizanov, A. Morozov, Effective categoricity of
  Abelian p-groups, arXiv:0805.1889 (2009).
- R. Alvir, B. Csima, L. MacLean, Scott Complexity of Reduced Abelian
  p-groups, arXiv:2407.06940 (2024).
- W. Calvert, The isomorphism problem for computable Abelian p-groups of
  bounded length, J. Symb. Logic (2005), math/0406505.
- D. Hirschfeldt, B. Khoussainov, R. Shore, A. Slinko, Degree spectra and
  computable dimensions in algebraic structures, Ann. Pure Appl. Logic (2002).
- A. Melnikov, New Degree Spectra of Abelian Groups, Notre Dame J. Formal
  Logic (2017).
- C. Jockusch, R. Soare, Pi^0_1 classes and degrees of theories (1972)
  minimal-pair black box; L. Fuchs, Infinite Abelian Groups (Ulm/Prufer).
