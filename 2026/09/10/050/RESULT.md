# Target conjunction is false: E1(Q) is empty and U_3(Z) is empty 2-adically

## Context

Let F3(x,y,z) = x^2+y^2+z^2+4(x^2y^2+y^2z^2+z^2x^2)-16x^2y^2z^2-3 (k=3),
W_3 its projective MK3 surface in (P^1)^3, U_3 = W_3 minus {rst=0} the affine
integral model over Z, and E1 the z=1 fibre 5x^2+5y^2-12x^2y^2-2=0.
The admitted target asked for (a) rank(E1(Q))<=2 via 2-descent/regulator after a
Q-point, (b) quaternion A1=(4x^2+1,-26) evaluation excluding a residue set S, and
(c) a bounded height window. Dao 2023 proves F3 Brauer obstructions only for
k=-(1+27l^2)/4<0 with narrow congruences, and its local-solubility proposition
needs k=1 mod 4; k=3 satisfies neither, leaving k=3 open.

## Definitions

- Squares mod 8 are {0,1,4}.
- For x=a/b in lowest terms (b>=1, gcd(|a|,b)=1) on E1, put
  u=12a^2-5b^2, v=5a^2-2b^2, N(a,b)=(2b^2-5a^2)(5b^2-12a^2)=uv
  = 60a^4-49a^2b^2+10b^4.
- U_3(Z/8): solutions of F3=3 with the -16 term vanishing mod 8.

## Result

**Theorem 1.** Affine E1(Q) is empty; its projective (2,2) closure has no
rational point either. Hence target clause (a) is ill-posed: E1 cannot be
viewed as an elliptic curve over Q and no regulator/2-descent rank certificate
of the required shape exists.

**Theorem 2.** U_3(Z/8) is empty; hence U_3(Z_2) is empty and U_3(Z) is empty
unconditionally. This is strictly stronger than the claimed Brauer sieve plus
height window, which become vacuous/moot.

## Proof / evidence

*Theorem 1.* From E1, y^2=(2b^2-5a^2)/(5b^2-12a^2)=v/u. Degeneracies
denominator 0, numerator 0, N=0 need a^2/b^2=5/12 or 2/5, impossible since
neither 5/12 nor 2/5 is a square in Q (60, resp. 10, nonsquare). So u,v nonzero
same sign and uv=N a positive square. Discriminant 49^2-4*60*10=1 gives
N=(12a^2-5b^2)(5a^2-2b^2). Since 5v-2u=a^2 and 12v-5u=b^2, any common divisor of
u,v divides coprime a^2,b^2, so u,v coprime; hence |u|,|v| each squares.
Negative branch u=-s^2,v=-t^2: b even gives t^2=3 mod 8; b odd forces a odd
(s^2=1) then t^2=5 mod 8; none squares. Positive branch: b even gives
v=5 mod 8; b odd gives u in {3,7,3} mod 8; none squares. Boundary r=0 or s=0
needs 5/12 square in Q, false. QED. Corroborated by exhaustive N=square search
to |a|,b<=3000 (0 hits).

*Theorem 2.* Mod 8, F3=3 is x^2+y^2+z^2+4(sum x^2y^2)=3. With a=x^2 etc. in
{0,1,4}: if some square is 0 then a+b+4ab takes only {0,1,4,5,6}, never 3; if
all nonzero, with n1 ones the total is 12-3n1+4*C(n1,2) giving 7,2,1,4 for
n1=3,2,1,0, never 3. A 2-adic point would reduce mod 8, so U_3(Z_2) and U_3(Z)
are empty. QED. Replayed exhaustively over 512 (U_3) + 64 (E1) classes:
PROOF_OK.

## Limitations

Disproves the target conjunction as stated; constructs no rank certificate,
Brauer table, or height constant since the objects do not exist. Does not
re-decide W_3 smoothness/Picard-18 or A1 Brauer status. Method specific to k=3.

## Reproducibility

- `output/artifacts/mod8_emptiness_proof.py` (stdlib only) prints PROOF_OK.
- `output/artifacts/e1_rational_search.py` (stdlib only) prints SEARCH_OK.
- Hand steps (factorization, gcd identities, mod-8 checks) verifiable by hand.

## References

- Quang-Duc Dao, Brauer-Manin obstruction for Wehler K3 surfaces of Markoff
  type, arXiv:2302.11515 (Thm 1.3 k<0 family; local-solubility needs k=1 mod 4).
- Quang-Duc Dao, Rational and integral points on Markoff-type K3 surfaces,
  arXiv:2504.10992 (different product family).
- Ghosh-Sarnak, Integral points on Markoff type cubic surfaces, Invent. 2022
  (cubic program; motivation only).
- Fuchs et al., Orbits on K3 Surfaces of Markoff Type (dynamics context).
