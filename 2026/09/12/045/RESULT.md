# Directed landscape geodesic: no deterministic uniform one-sided transversal modulus with constant 6

## Context

Let $\mathcal L$ be the directed landscape and $g:[0,1]\to\mathbb R$ the almost
surely unique finite geodesic from $(0,0)$ to $(0,1)$, so $g(0)=0$.
For $s\in(0,1]$ define

$$K(s)=6\,s^{2/3}(\log(1/s))^{1/3},\qquad
  M(s)=\sup_{t\in[0,1-s]}(g(t+s)-g(t))_+,$$

with $(a)_+=\max(a,0)$. The admitted target question was whether there exists
a deterministic $s_0>0$ such that

$$\mathbb P\bigl(M(s)\le K(s)\ \forall\,0<s\le s_0\bigr)=1.\tag{*}$$

The exponents $(2/3,1/3)$ are the KPZ transversal/log-correction scaling, and
the constant $6$ was the proposed uniform modulus constant. The directed
landscape is known (Dauvergne-Ortmann-Virag) to have a.s. continuous sample
paths, independent time increments, Airy line ensemble slices, and a.s. unique
geodesics between fixed endpoints that are Holder-$2/3^-$ continuous with a
random constant.

## Definitions

- Directed landscape $\mathcal L$: continuous four-parameter random field with
  metric composition and independent increments.
- Geodesic $g$: a.s. unique maximizer path from $(0,0)$ to $(0,1)$.
- One-sided modulus $M(s)$: worst rightward increment over window $s$.
- Deterministic $s_0$: a non-random scale below which the bound is required
  to hold simultaneously with probability one.

## Result

**Theorem.** For every deterministic $s_0>0$,

$$\mathbb P\bigl(M(s)\le K(s)\ \forall\,0<s\le s_0\bigr)<1.$$

Hence the statement $(*)$ is false: no deterministic $s_0>0$ makes the uniform
one-sided bound with constant $6$ hold almost surely. In fact the proof shows
the stronger per-scale full support: for every fixed $s\in(0,1)$ and every
finite $M_0$, $\mathbb P(g(s)>M_0)>0$.

## Proof / evidence

Two lemmas give the result. Full details are in the draft; the argument uses
only standard black-box inputs (DOV continuity, increment independence,
geodesic existence; Airy-slice Brownian Gibbs property of Corwin-Hammond;
Brownian bridge tube support).

**Lemma 1 (deterministic tube).** Let $\mu$ be a Brownian bridge law on
$[l,r]$ from $(l,u)$ to $(r,v)$ with $u,v$ strictly above a continuous floor
$f$. Then $\mu(\text{stay above }f)>0$ and $\mu(\{B(a)>T\}\cap\{\text{above }f\})>0$
for any interior $a$ and level $T$. Proof: construct an explicit
piecewise-linear $h$ through $(l,u)\to(a,P)\to(r,v)$ with peak $P$ large enough
that $h>f$ everywhere and $h(a)\ge T$, then use positive bridge mass on a
narrow uniform tube around $h$.

**Lemma 2 (single-scale positivity).** Fix $s\in(0,1)$, $M_0\in\mathbb R$.
Write $F(x)=\mathcal L(0,0;x,s)$, $G(x)=\mathcal L(x,s;0,1)$, $H=F+G$.
Put $a=M_0+1$, $I=[M_0+1/2,M_0+3/2]$, $S=\sup_{x\le M_0}H(x)$.
Condition on $\mathcal F=\sigma(F,G|_{I^c},\underline G|_I)$ where
$\underline G$ is the second Airy line. By increment independence $F$ is
independent of $(G,\underline G)$; by Brownian Gibbs the conditional law of
$G|_I$ is a bridge conditioned to stay above $\underline G|_I$ with a.s.
admissible data. Lemma 1 gives conditional probability
$p(\mathcal F)=\mathbb P(H(a)>S\mid\mathcal F)>0$ a.s., hence mean $>0$, so
$\mathbb P(g(s)>M_0)\ge\mathbb P(H(a)>S)>0$.

**Theorem derivation.** Given $s_0>0$ set $s^\star=\min(s_0,1/2)$ and
$y^\star=K(s^\star)+1$. Lemma 2 gives $p^\star=\mathbb P(g(s^\star)>y^\star)>0$.
Since $g(0)=0$, $\{g(s^\star)>y^\star\}\subset\{M(s^\star)>K(s^\star)\}$, so the
all-scales event has probability at most $1-p^\star<1$.

## Limitations

The falsity targets exactly the deterministic-$s_0$ quantifier as written. It
does not construct an a.s. sequence of violating scales $s_n\to0$; the draft
notes such a sequence should not exist because a random-$s_0(\omega)$ modulus
with constant below $6$ plausibly holds by standard tail bounds plus dyadic
chaining (remark/conjecture, not claimed). The proof cites standard
directed-landscape inputs as black boxes rather than re-proving them.

## Reproducibility

The draft proof is self-contained given the cited black boxes. The supporting
script `verify_chaining_constants.py` checks the chaining-constant arithmetic
($c_1=1/32$, threshold $A>3.17$ for natural log and $>4.19$ for $\log_{10}$,
both below $6$) behind the Section 5 remark and runs with standard Python 3
without dependencies.

## References

- Dauvergne-Ortmann-Virag, The directed landscape, Acta Math. 229 (2022),
  arXiv:1812.00309.
- Corwin-Hammond, Brownian Gibbs property for Airy line ensembles.
- Morters-Peres, Brownian Motion (bridge support / small-ball positivity).
- Dauvergne-Sarkar-Virag, Three-halves variation of geodesics, Ann. Probab.
  50 (2022).
- Spivak, One-point large deviations of the directed landscape geodesic,
  arXiv:2503.09486.
- Dauvergne, The 27 geodesic networks in the directed landscape (2025).
