# Associativity-certified census of rank-5 multiplicity-free fusion rings with Frobenius-Perron dimension at most 12

## Context

Fusion rings are the Grothendieck rings of fusion categories and the algebraic backbone of subfactor, modular-category and topological-phase (anyon) classification. Concrete low-rank catalogs are cited as benchmarks for tensor-category software (Anyonica/anyonwiki), yet the multiplicity-free census to rank 7 is explicitly conditional on correctness/completeness of a single Wolfram pipeline (Vercleyen 2025). An independent integer-arithmetic certificate for one Frobenius-Perron-bounded stratum closes a citable gap and gives reusable dimension-polynomial checks.

## Definitions

Rank-5 based ring: free Z-module with basis X0=1,X1,...,X4, products Xi*Xj=sum_k N_{ij}^k Xk with N_{ij}^k in {0,1} (multiplicity-free), N_{0i}^j=delta_{ij}, duality involution * with 0*=0 and N_{ij}^0=delta_{j,i*}. Fusion matrices (Ni)_{j,k}=N_{ij}^k. Associativity is Ni*Nj=sum_k N_{ij}^k Nk (25 identities), equivalently sum_m N_{ij}^m N_{mk}^l=sum_m N_{jk}^m N_{im}^l. Based-ring isomorphism is a permutation fixing 0 with p(*i)=*p(i) conjugating N. Frobenius-Perron dimension: M=sum_i Ni has Perron eigenvalue lam=sum_i di; d normalized d0=1 is the common eigenvector Ni*d=di*d; D=sum_i di^2.

Duality types up to Stab(0): self-dual (0,1,2,3,4) nfix=5, one-pair (0,2,1,3,4) nfix=3, two-pair (0,2,1,4,3) nfix=1. Allowed perm sizes 24/4/8. Lex-min flattened tuple is the normal form.

## Result

**Theorem (verified census).** Up to based-ring isomorphism there are exactly 7 multiplicity-free rank-5 fusion rings with D<=12. They are all commutative. In full there are exactly 16 isomorphism types at any D (10 self-dual +5 one-pair +1 two-pair), all commutative; 9 lie at D>12 and are excluded by certified rational lower bounds. In particular there is no noncommutative multiplicity-free rank-5 Frobenius-reciprocal ring at any D, hence none at D<=12.

The 7 types in lex-min normal form:

- (a) Pointed cyclic Z(C5): star [0,2,1,4,3], d=(1,1,1,1,1), D=5, M charpoly lam^4(lam-5), Perron 5.
- (b1) TY(Z2xZ2): star [0,1,2,3,4] self-dual, d=(1,1,1,2,1) up to perm, D=8, charpoly lam^3(lam-6)(lam-2), Perron 6.
- (b2) TY(Z4): star [0,2,1,3,4] one-pair, d=(1,1,1,2,1) up to perm, D=8, same charpoly.
- (c1,c2) sqrt17 pair: one self-dual + one one-pair, d=(1,1,1,(1+sqrt17)/2,1) up to perm, D=(17+sqrt17)/2 approx 10.56155281, M charpoly lam^3(lam^2-9lam+16), Perron (9+sqrt17)/2 approx 6.56155281.
- (d1,d2) D=12 pair: one self-dual with d=(1,1,sqrt3,2,sqrt3) up to perm + one one-pair with d=(1,sqrt3,sqrt3,1,2), D=12 exactly, M charpoly lam^2(lam-1)(lam^2-8lam+4), Perron 4+2sqrt3 approx 7.46410161.

Raw counts before quotient: 132+10+2=144 associative tables from 1118208 Frobenius tables (2^20+2^16+2^12); D<=12 raw 20+6+2=28; iso 3+3+1=7. Full 5x5x5 arrays, M, charpoly and SHA256 per type are in output/artifacts/tables.json; Sec.5 of draft lists all Ni matrices. Witnesses: commutative pointed witness is Z5 (all Ni permutation matrices); D=8 pair are Tambara-Yamagami; smallest non-TY non-pointed in stratum is D=(17+sqrt17)/2; stratum maximum is D=12. Noncommutative witness collapses by exclusion: all 16 types verified commutative (self-dual case is theorem).

## Proof / Evidence

1. Frobenius necessity: tau(sum c_l Xl)=c_0 gives tau(XiXj)=delta_{j,i*}, tau((XiXj)Xk)=N_{ij}^{k*}, tau(Xi(XjXk))=N_{jk}^{i*}, so associativity forces N_{ij}^{k*}=N_{jk}^{i*} and orbit generators f1:(i,j,k)->(i*,k,j), f2:(k,j*,i), f3:(j*,i*,k*). Enumerating only Frobenius-constant tables loses no associative rings. Self-dual implies N_{ij}^k=N_{ji}^k, hence commutative.
2. Enumeration: build orbits (35/30/25 total, 15/14/13 fixed, 20/16/12 free), enumerate 1048576+65536+4096 tables chunkwise (numpy int8/int16 exact, values <=5), filter nonempty (necessary since di*dj>0), progressive exact check on 16 pairs i,j>=1 (pairs with 0 trivial since N0=I) then pure-Python recheck on all 25 pairs. Survivors 132/10/2. Canonicalize by lex-min under duality-preserving perms (24/4/8) giving 10+5+1=16 types. D is iso-invariant.
3. FP certificate: M strictly positive for all 7 D<=12 types (all-ones except (3,3) entry 3-5), hence primitive. Integer charpolys (sympy Faddeeva/Bareiss) factor as above. Linear factors give exact Perron; quadratics lam^2-9lam+16 (disc 17) and lam^2-8lam+4 (disc 48) bisected in [6,7] resp [7,8] with exact Fraction evaluation to width <6e-08 (<1e-6 required). Exact dims in Q/Q(sqrt17)/Q(sqrt3) checked Ni*d=di*d by sympy (x^2=x+4 for (1+sqrt17)/2); D is 5,8,(17+sqrt17)/2 (<11 since sqrt17<5),12. M irreducible => exhibited positive eigenvector is the PF vector.
4. Exclusion D>12: for each of 9 high types pick positive rational x (approx PF vector rounded to denom 2000) and compute li=min_j (Ni*x)_j/x_j in Fractions, L=sum li^2. Collatz-Wielandt (Ni*x>=mu*x => rho(Ni)>=mu by iteration) gives di>=li and D>=L. All 9 give L>12 (14,16.6044,24,26.1795,30.1376,31.0894,34.6427; min margin 2).
5. Commutativity checked N_{ij}^k==N_{ji}^k for all 16 canonicals (hence all 144 raw by iso-invariance).

## Limitations

Scope is multiplicity-free (N in {0,1}) rank-5 Frobenius-reciprocal only; higher multiplicities/ranks out of scope (non-Frobenius impossible under associativity by lemma). Ring-level classification only; pentagon/F-symbols and categorifiability not addressed. D is ring-level FP dimension. Literature comparison is qualitative without table import; exact matching to Vercleyen appendix / Liu-Palcoux-Ren labels left to future work. High-D bounds sound but not tight. No new analytic bound or anyon model is claimed; novelty is the independent closure certificate.

## Reproducibility

`python3 output/artifacts/verify.py` (~2s on laptop CPU, <600s required) re-enumerates 1118208 tables, re-verifies 25 residuals, charpolys, intervals, lower bounds, SHA. Deps: Python stdlib + numpy (integer-matmul only, all decisions exact) + sympy (exact charpoly/sqrt). No Wolfram/Anyonica. Writes `tables.json` with 7+9 canonical tables (N, M, charpoly, SHA). Log shows raw 132+10+2=144, iso 10+5+1=16, D<=12 3+3+1=7, all commutative, widths <6e-08.

## References

- G. Vercleyen and J. Slingerland, On Low Rank Fusion Rings, arXiv:2205.15637 (2022). Generates fusion rings to order 9, introduces songs generalizing TY/HI, Wolfram package and data website.
- G. Vercleyen, On Low-Rank Multiplicity-Free Fusion Categories, PhD thesis, arXiv:2405.20075 (2024). Algorithms, Anyonica solving, appendices listing multiplicity-free rings to rank 9 and categories to rank 7.
- G. Vercleyen, Tables of practical invariants for distinguishing multiplicity-free fusion categories up to rank 7, arXiv:2507.00652 (2025). Flags Anyonica/anyonwiki census as conditional, resolves inequivalence conditionally.
- Z. Liu, S. Palcoux and Y. Ren, Classification of Grothendieck rings of complex fusion categories of multiplicity one up to rank six, Lett. Math. Phys. 112:54 (2022). doi:10.1007/s11005-022-01542-1. Categorifiable multiplicity-one classification to rank six.
