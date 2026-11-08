# Independent mathematical audit

## correctness

PASS

For F=GF(2^m), g=gcd(m,r), s=2^g, n=m/g and D=2^r+1, write each triple summing to first coordinate a as (a+u,a+v,a+u+v); its second-coordinate deviation from a^D equals B(u,v)=u^(2^r)v+uv^(2^r). For v!=0, B(vt,v)=v^D(t^(2^r)+t). The image of this additive linear polynomial is H=ker Tr(F/F_s), of size q/s. If n odd, gcd(D,q-1)=1, so scaled H covers F (except n=1), with exact ordered triple counts q+(q-1)s on b=a^D and q-s otherwise. If n=2, H=F_s and the D-power image is F_s^*, giving 3G=F x F_s; n=1 graph itself additive. For even n>=4, D-power subgroup P has index s+1; when n has odd divisor e>=3, F_(s^e)^* lies in P and each coset meets H by a nonzero trace kernel vector. If n is a power of two >=4, F_(s^2) is contained in H, and its nonzero elements project onto all s+1 cosets of P. Therefore 3G=F^2 for n>=3. Direct 2G fibers give |2G|=1+(q-1)q/s, so the covering threshold 3 is sharp. Independently brute-enumerated finite fields degrees m<=6 with r<=m using checked polynomial-basis arithmetic and confirmed the claimed supports and twofold cardinalities; infinite result rests on trace/coset argument.

## originality

PASS

Thornburgh 2024 Thm 1.6 covers three-distinct-point sum multiplicities for binary Gold APN functions with gcd(m,r)=1 and even m, which already implies full triple support for that APN subfamily. The present contribution is the uniform classification including gcd(m,r)>1 and even relative degree >=4, the exceptional n1,n2 cases and the |2G| formula. Carlet–Gong–Tan derivative uniformity and the published Resultary Gold-graph fourth-moment result provide relevant machinery but not an equivalent general 3G support theorem.

## value

PASS

Additive diameter and threefold sum representation of Gold-polynomial graphs are natural invariants in characteristic-two finite-field combinatorics. The phase split by relative Frobenius order and the non-APN full-coverage proof are structurally motivated and give a complete sharp classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
