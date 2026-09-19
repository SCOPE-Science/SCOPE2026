# Cyclotomic Hensel roots form an exact 2-adic prime-support isometry

## Statement

Let \(\Phi_n\) be the \(n\)-th cyclotomic polynomial and let \(\nu_2\) be
the normalized \(2\)-adic valuation.  For every squarefree integer \(n>1\),
there is a unique
\[
\beta_n\in 2\mathbb Z_2
\]
such that
\[
\Phi_n(\beta_n)=-1.
\]
These roots encode the complete squarefree prime support, not merely its least
prime.

If \(m,n>1\) are distinct squarefree integers, then
\[
\boxed{\;
\nu_2(\beta_m-\beta_n)
=
\min\{p:\ p\text{ divides exactly one of }m,n\}.
\;}
\tag{1}
\]
Equivalently, if \(P(n)\) denotes the set of prime divisors of \(n\),
\[
|\beta_m-\beta_n|_2
=
2^{-\min(P(m)\triangle P(n))}.
\]

It is useful to adjoin the empty prime support by setting
\[
\beta_\varnothing:=2.
\]
Then (1) remains valid for all distinct finite sets of primes \(S,T\), with
\(\beta_S:=\beta_{\prod_{p\in S}p}\) for \(S\neq\varnothing\):
\[
\boxed{\;
\nu_2(\beta_S-\beta_T)=\min(S\triangle T).
\;}
\tag{2}
\]

There is also a complete even-base valuation formula.  For every even
\(x\in\mathbb Z_2\) and every \(n>1\),
\[
\boxed{
\nu_2(\Phi_n(x)+1)=
\begin{cases}
\nu_2(x-\beta_n),&n\text{ squarefree},\\[1mm]
1,&n\text{ nonsquarefree}.
\end{cases}}
\tag{3}
\]

Thus \(n>1\) is squarefree if and only if the equation
\[
\Phi_n(X)=-1
\]
has a solution in \(2\mathbb Z_2\), and in the squarefree case the solution is
unique.

## Prime-support Cantor set

Put
\[
d(S,T)=2^{-\min(S\triangle T)}
\]
for distinct sets of primes \(S,T\).  Formula (2) says that the finite prime
subsets embed isometrically into \(\mathbb Z_2\).  Completing this metric
space gives all subsets of the primes, so the map extends uniquely to an
isometric embedding
\[
\widehat\beta:\mathcal P(\{\text{primes}\})\longrightarrow 2\mathbb Z_2.
\]

Let \(\mathcal C\) be its image and, for an integer \(B\ge2\), let \(N_B\)
be the number of residue classes modulo \(2^B\) met by \(\mathcal C\).
Then
\[
\boxed{\;N_B=2^{\pi(B-1)}.\;}
\tag{4}
\]
Indeed, two supports give the same residue modulo \(2^B\) exactly when they
agree on every prime \(p<B\).  Consequently
\[
\frac{N_{B+1}}{N_B}
=
\begin{cases}
2,&B\text{ prime},\\
1,&B\text{ composite},
\end{cases}
\tag{5}
\]
so the residue tree branches exactly at prime depths.

The set \(\mathcal C\) is uncountable but has Haar measure zero and
\(2\)-adic box dimension zero.  At depth \(B\) it is covered by
\(2^{\pi(B-1)}\) balls of radius \(2^{-B}\), whose total Haar measure is
\[
2^{\pi(B-1)-B}\longrightarrow0,
\]
and \(\pi(B)/B\to0\) gives box dimension zero.

## A single 2-adic prime-sequence limit

Let \(p_1<p_2<\cdots\) be the primes, let
\[
P_k=\prod_{j\le k}p_j,\qquad P_0=1,
\]
and set \(\beta_{P_0}=2\).  Formula (2) gives
\[
\nu_2(\beta_{P_{k+1}}-\beta_{P_k})=p_{k+1}.
\]
Hence \((\beta_{P_k})\) is Cauchy in \(\mathbb Z_2\); write
\[
\Xi=\lim_{k\to\infty}\beta_{P_k}.
\]
Because the successive valuations \(p_{k+1}\) are strictly increasing,
\[
\boxed{\;
\nu_2(\Xi-\beta_{P_k})=p_{k+1}\qquad(k\ge0).
\;}
\tag{6}
\]
Thus the full prime sequence is recoverable recursively from one \(2\)-adic
limit and the cyclotomic Hensel roots of the already recovered primorials.
This is an exact local analogue of prime-sequence encoding by a limiting
cyclotomic quantity; no claim of computational efficiency is intended.

## Fixed even bases

Every squarefree \(\beta_n\) satisfies
\[
\beta_n\equiv2\pmod4.
\]
Therefore a fixed even integer \(x\) detects squarefreeness through
\(\nu_2(\Phi_n(x)+1)>1\) for every \(n>1\) if and only if
\[
\boxed{x\equiv2\pmod4.}
\tag{7}
\]
For \(x\equiv0\pmod4\), both squarefree and nonsquarefree indices give
valuation \(1\).

The base-\(2\) least-prime extractor is recovered as
\[
\nu_2(\beta_n-2)=\operatorname{lpf}(n)
\qquad(n>1\text{ squarefree}).
\tag{8}
\]
More generally, put \(x=2+2^B\) with \(B\ge2\), and let
\(p=\operatorname{lpf}(n)\).  For squarefree \(n\),
\[
\nu_2(\Phi_n(2+2^B)+1)=
\begin{cases}
p,&p<B,\\
> B,&p=B,\\
B,&p>B.
\end{cases}
\tag{9}
\]
In particular, when \(B\) is composite the valuation is exactly
\(\min(p,B)\).

## Proof

For squarefree \(n>1\), the Taylor expansion at the origin is
\[
\Phi_n(X)=1-\mu(n)X+X^2H_n(X),
\qquad H_n\in\mathbb Z[X].
\tag{10}
\]
Let
\[
F_n(X)=\Phi_n(X)+1.
\]
For \(u,v\in2\mathbb Z_2\), polynomial division of the difference gives
\[
\Phi_n(u)-\Phi_n(v)=(u-v)U_n(u,v),
\]
where
\[
U_n(u,v)\equiv-\mu(n)\equiv1\pmod2.
\]
Every contribution to \(U_n\) from a monomial of degree at least \(2\)
contains a positive power of \(u\) or \(v\), hence is even.  Therefore
\[
\boxed{\;
\nu_2(F_n(u)-F_n(v))=\nu_2(u-v)
\quad(u,v\in2\mathbb Z_2).
\;}
\tag{11}
\]

Now \(F_n(0)=2\equiv0\pmod2\) and
\(F_n'(0)=-\mu(n)\) is a \(2\)-adic unit.  Hensel's lemma gives a root
\(\beta_n\in2\mathbb Z_2\), and (11) makes it unique.  Applying (11) to
\(\beta_n\) and \(0\) shows
\[
\nu_2(\beta_n)=\nu_2(F_n(0))=1,
\]
so \(\beta_n\equiv2\pmod4\).  Formula (11) with \(v=\beta_n\) proves the
squarefree half of (3).

If \(n\) is nonsquarefree, write
\[
r=\operatorname{rad}(n),\qquad a=n/r\ge2.
\]
Radical reduction gives
\[
\Phi_n(X)=\Phi_r(X^a).
\]
For even \(x\), equation (10) applied to \(r\) yields
\[
\Phi_n(x)+1
=
2-\mu(r)x^a+x^{2a}H_r(x^a)
\equiv2\pmod4.
\]
This proves the nonsquarefree half of (3), and also the squarefreeness
criterion.

It remains to prove the prime-support metric.  Let \(n>1\) be squarefree and
let \(q\nmid n\) be prime.  The standard cyclotomic identity
\[
\Phi_{nq}(X)=\frac{\Phi_n(X^q)}{\Phi_n(X)}
\tag{12}
\]
gives, at \(X=\beta_n\),
\[
F_{nq}(\beta_n)
=
1-\Phi_n(\beta_n^q).
\tag{13}
\]
Since \(\nu_2(\beta_n)=1\), (10) gives
\[
\nu_2\bigl(\Phi_n(\beta_n^q)-1\bigr)=q.
\]
Using the isometry (11) for \(F_{nq}\) therefore gives the exact one-prime
toggle law
\[
\boxed{\;
\nu_2(\beta_{nq}-\beta_n)=q.
\;}
\tag{14}
\]

For a singleton support \(\{q\}\),
\[
F_q(2)=\Phi_q(2)+1=2^q,
\]
so (11) gives
\[
\nu_2(\beta_q-2)=q.
\tag{15}
\]
Starting from any finite support and toggling one prime at a time, (14) and
(15) show that the increments have valuations equal to the toggled primes.
Along a path from \(S\) to \(T\), every prime of \(S\triangle T\) is toggled
exactly once.  The smallest such prime therefore occurs exactly once among
the increments.  The ultrametric inequality, with uniqueness of the smallest
valuation, gives
\[
\nu_2(\beta_S-\beta_T)=\min(S\triangle T),
\]
proving (2) and hence (1).  Equations (4)--(9) follow immediately.

## Relation to recent work

Shunia's 2026 preprint *Cyclotomic Prime Extractors* proves, for \(n>1\),
\[
\nu_2(\Phi_n(2)+1)=
\begin{cases}
\operatorname{lpf}(n),&n\text{ squarefree},\\
1,&n\text{ nonsquarefree},
\end{cases}
\]
and explicitly notes that the choice of the base \(2\) matters for this
plus-sign identity.  It then recovers further prime factors through an
Archimedean logarithmic peeling mechanism.

The present result identifies a different local mechanism: varying the
squarefree index changes a unique even Hensel root by exactly the prime being
toggled.  This upgrades a least-prime valuation at one integer base to an
exact \(2\)-adic geometry of the entire prime support, gives the complete
even-base formula (3), and yields the residue-complexity identity (4).

## Verification

`artifacts/verify_hensel_fingerprints.py` uses exact integer arithmetic and
SymPy 1.14.0 cyclotomic polynomials.  It independently lifts the unique even
root modulo powers of \(2\) and checks:

- all squarefree \(2\le n\le300\), giving 182 lifted roots modulo \(2^{64}\);
- 15,344 unordered pairs for which the first differing prime is below \(64\),
  verifying (1);
- 8,159 pairs \((n,x)\) with \(2\le n\le200\) and even
  \(-40\le x\le40\), verifying (3);
- the exact count \(2^{\pi(B-1)}\) of root residues for every
  \(3\le B\le12\).

The output is recorded in `artifacts/verification.txt`.  These computations
are supporting checks; the theorem is proved above without finite
enumeration.

## Originality and limitations

Originality is asserted only to the best of our knowledge.  The relevant
local sections of Shunia's arXiv:2609.18480v1 were inspected: they establish
the base-\(2\) valuation and the first-term expansion used above, but do not
state a Hensel-root parametrization, the one-prime toggle law (14), the
symmetric-difference isometry (1), or the prime-controlled residue tree (4).

Herrera-Poyatos and Moree survey coefficient and derivative formulas for
cyclotomic polynomials, including the standard identity (12) and expansions
at the origin.  Their inspected text contains no \(p\)-adic or Hensel-root
treatment.  Pomerance and Rubinstein-Salzedo study real coincidences
\(\Phi_m(x)=\Phi_n(x)\), rather than roots of \(\Phi_n(x)+1\) in
\(\mathbb Z_2\).

Searches for exact and synonymous formulations involving cyclotomic Hensel
roots, \(2\)-adic roots of \(\Phi_n(X)+1\), prime-support ultrametrics,
symmetric differences of prime supports, and \(2\)-adic cyclotomic
fingerprints did not identify prior coverage.  No specific inaccessible
paper was found whose title or indexed statement suggests the same theorem.
The motivating preprint is only days old, so contemporaneous unindexed work
is the principal residual originality risk; older poorly indexed local
cyclotomic literature remains a secondary risk.

The result concerns the prime \(2\) and the equation \(\Phi_n(X)=-1\).
It does not assert an analogous isometry for odd \(p\)-adic completions, does
not provide an efficient factorization algorithm, and does not improve
bounds for ordinary cyclotomic coefficients.

## References

1. Joseph M. Shunia, *Cyclotomic Prime Extractors*, arXiv:2609.18480v1,
   2026. https://arxiv.org/abs/2609.18480
2. Carl Pomerance and Simon Rubinstein-Salzedo, *Cyclotomic Coincidences*,
   Experimental Mathematics 31 (2022), 596--605.
   https://doi.org/10.1080/10586458.2019.1660741
3. Andrés Herrera-Poyatos and Pieter Moree, *Coefficients and higher order
   derivatives of cyclotomic polynomials: old and new*, Expositiones
   Mathematicae 39 (2021), 309--343. https://arxiv.org/abs/1805.05207
