# Cyclotomic p-adic Heegner height on 37a1 over Q(sqrt(-11)) at p = 5: nonvanishing

## Context

Let E be the elliptic curve 37a1, the canonical rank-one Gross-Zagier curve: the
curve of minimal conductor with positive rank. Let f be the weight-2 newform of
level 37. Let K = Q(sqrt(-11)), in which both 37 and 5 split, so the Heegner
hypothesis for X_0(37) and the split-ordinary hypothesis at p = 5 hold. Let P in
E(K) be the classical Heegner point of discriminant -11, known to be of infinite
order classically. The Perrin-Riou-Disegni cyclotomic p-adic Gross-Zagier
formula relates the cyclotomic p-adic height h_p(P) to the cyclotomic derivative
of the Rankin-Selberg p-adic L-function at the trivial character. The question
is whether h_p(P) is nonzero, equivalently whether the cyclotomic derivative is
nonzero, giving the rank-one p-adic Birch-Swinnerton-Dyer consequence at this
minimal ordinary split triple.

## Definitions

- Curve: E: y^2 + y = x^3 - x (Cremona 37a1), minimal model
  `ellinit([0,0,1,-1,0])`, conductor 37, discriminant 37, split multiplicative
  reduction at 37.
- Quadratic twist by -11: minimal model E^(-11) = `ellinit([0,0,1,-121,-333])`,
  conductor 4477 = 11^2 * 37.
- K = Q(sqrt(-11)). Both 5 and 37 split in K: 5 = p5*p5bar,
  37 = p37*p37bar (verified by Kronecker symbols and idealfactor).
- a_5(E) = -2, so E has good ordinary reduction at 5. Hecke polynomial
  X^2 + 2X + 5 with unit root alpha = 3 + 2*5 + 4*5^2 + ... and non-unit root
  beta = 2*5 + 2*5^3 + ... .
- p-adic height: PARI `ellpadicheight(E,p,n,P)` raw vector in the basis
  (omega, eta = x*omega) of H^1_dR; the canonical cyclotomic height is
  h = f - s2*g with s2 = `ellpadics2(E,p,n)`, i.e. `ellpadicregulator` for
  rank one. This is the normalization in which PARI's `ellpadicbsd` is stated.
- p-adic L-function: PARI `ellpadicL` (alpha-branch, ordinary projection) and
  derivatives `ellpadicL(E,p,n,0,r)`; `ellpadicbsd` returns [rank, L-value].

## Result

With the above notation, for E = 37a1, K = Q(sqrt(-11)), p = 5:

1. a_5 = -2 (good ordinary); 37 and 5 split in K; the Heegner and
   split-ordinary hypotheses hold.
2. The classical Heegner point P of discriminant -11 has infinite order:
   rank E(Q) = 1, rank E^(-11)(Q) = 0, hence rank E(K) = 1, with trivial
   torsion over Q and over K; `ellheegner(E) = [0,0]` of nonzero complex
   height, and [-1,0] = -3*[0,0].
3. The cyclotomic p-adic height h_p(P) is nonzero, and equivalently the
   cyclotomic derivative L_p^{cyc'}(f/K, 1) is nonzero. Hence
   ord_1 L_p^{cyc}(f/K) = 1 and the p-adic regulator does not vanish: the
   rank-one p-adic BSD consequence holds at this triple.
4. Explicit value: on the Q-generator (0,0),
   R_p((0,0)) = 5 + 5^2 + 5^3 + 3*5^6 + 4*5^7 + 5^9 + 5^10 + O(5^11),
   of 5-adic valuation exactly 1. The Mazur-Tate-Teitelbaum derivative is
   2*5 + 2*5^2 + 2*5^4 + ... (valuation 1); the ordinary Euler factor
   (1 - alpha^{-1})^{-2} = 1 + 5^2 + 3*5^3 + ... is a 5-adic unit.

## Proof / evidence

Classical rank: PARI 2.17.2 exact routines give `ellrank(E) = [1,1,0,[[-1,0]]]`
and `ellrank(E^(-11)) = [0,0,0,[]]`, so rank E(K) = 1 + 0 = 1 by the twist-rank
formula; `elltors` is trivial over Q and over K. Analytic cross-check:
`ellanalyticrank(E) = [1, 0.30599...]`, `ellanalyticrank(E^(-11)) = [0,
1.47824...]`, so L(E/K,s) has a simple zero with L'(E/K,1) approx 0.45234 != 0;
by Gross-Zagier the Heegner point has nonzero complex height, hence infinite
order. Explicitly `ellheegner(E) = [0,0]` with complex height 0.05111... != 0
and `ellmul(E,[0,0],-3) == [-1,0]` with height ratio exactly 9.

Ordinary stabilization: a_5 = -2 verified by #E(F5) = 8. Hensel roots
alpha (unit) and beta (valuation 1) satisfy alpha + beta = -2, alpha*beta/5 = 1.
The Euler factor (1 - alpha^{-1})^{-2} is a 5-adic unit, so alpha-stabilization
contributes no zero or pole at the trivial character.

Nonvanishing computation: `ellpadicheight(E,5,10,[0,0])` gives the raw vector;
the canonical projection gives (star) above. This is a proof of nonvanishing
because: (i) valuation gap: v_5 = 1 while the error modulus is O(5^11), and a
quantity 5*u + O(5^N) with u a unit and N >= 2 cannot be zero; (ii) stability:
n = 6, 8, 10 give identical truncations 5+5^2+5^3+3*5^6+O(5^7),
...+4*5^7+O(5^9), (star); (iii) quadraticity controls: H(2P) - 4H(P) = 0 to
working precision, R(8P)/R(P) = 64 (verified as 4+2*5+2*5^2 in 5-adics),
R((-1,0))/R((0,0)) = 9 = 3^2 matching the proved index-3 relation;
(iv) logarithm check: `ellpadiclog(E,5,10,8*(0,0))` has valuation 1, nonzero as
required (8*(0,0) lies in the formal group since #E(F5) = 8).

Transfer to K: since E(Q) has finite index in E(K) (equal ranks, trivial
torsion) and the cyclotomic height is quadratic with standard base-change
compatibility up to a nonzero rational factor, any infinite-order P in E(K),
in particular the Heegner point P = m*G (m != 0), satisfies h_p(P) != 0, with
h_p(P) = m^2*c*R_p((0,0)) for explicit nonzero scalar c.

Derivative side: L_p(E,1) = O(5^8) (vanishes, as L(E,1) = 0);
L_p'(E,1) = 2*5 + 2*5^2 + 2*5^4 + ... nonzero;
`ellpadicbsd(E,5,8) = [1, 5+5^2+5^3+...]` matches the regulator;
`ellpadicbsd(E^(-11),5,8) = [0, unit]`. Since 5 splits in K,
L_p(f/K)|_cyc = L_p(f)*L_p(f tensor eps_K) up to nonzero split Euler factors,
so its derivative at 1 is (valuation 1)*(unit) != 0. The equivalence
h_p(P) != 0 iff derivative != 0 is both the Perrin-Riou-Disegni theorem in this
verified good-ordinary split case and an independently computed fact.

## Limitations

- The nonvanishing certification rests on PARI/GP's Coleman-Gross/Bernardi
  height and Mazur-Stickelberger L-value implementation with tracked O(5^N)
  precision plus the stability and quadraticity self-checks above; it is not a
  hand-verified formal proof of that library code. This is the bounded
  Coleman-Gross computation leg explicitly allowed by the admitted target.
- The h_p-to-derivative equivalence cites the Perrin-Riou-Disegni cyclotomic
  p-adic Gross-Zagier theorem in the verified good-ordinary split case; both
  sides are additionally verified nonzero independently.
- The transfer uses PARI's proved 2-descent rank bounds and standard
  quadraticity and base-change compatibility of the cyclotomic height.

## Reproducibility

Tool: PARI/GP 2.17.2 via cypari2 (stack raised to 1 GB for
`ellpadicL`/`ellpadicbsd`). Command list in
`artifacts/reproducibility.json`; verbatim outputs in
`artifacts/pari_results.json`. Key one-liners:
`E=ellinit([0,0,1,-1,0]); ellpadics2(E,5,10);
ellpadicheight(E,5,10,[0,0]); ellpadicregulator(E,5,10,[[0,0]]);
ellpadicL(E,5,8,0,1); ellpadicbsd(E,5,8);`

## References

- Perrin-Riou; Disegni, The p-adic Gross-Zagier formula on Shimura curves
  (Compositio 2017), and universal sequel; Kobayashi (supersingular case);
  Castella; Buyukboduk-Pollack-Sasaki (critical slope).
- Balakrishnan-Ciperiani-Stein, p-adic heights of Heegner points and
  Lambda-adic regulators (Math. Comp. 2015): computational method and
  examples on other curves (57a1, 331a1), none covering this triple.
- Belabas-Bernardi (PARI p-adic height/sigma implementation); PARI/GP 2.17.2
  `ellpadicheight`, `ellpadicregulator`, `ellpadicL`, `ellpadicbsd`, `ellheegner`.
- LMFDB record 37.a1 for classical invariants of 37a1.
