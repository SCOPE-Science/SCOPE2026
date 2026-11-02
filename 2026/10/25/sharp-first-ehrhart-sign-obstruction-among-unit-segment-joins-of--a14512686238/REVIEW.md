# Independent mathematical audit

## correctness

PASS

For a_i positive integers, B=product_{i=1}^4[0,a_i], J=B*[0,1] embedded in Z^6 with the stated primitive join-height lattice, slice at integer height h in tJ gives (h+1)prod_i(a_i(t-h)+1), so L_J(t)=sum_{k=0}^t(t-k+1)prod_i(a_i k+1)=sum_{j=0}^4 e_j F_j(t). Exact degree-six power sums F_j show only the degree-one monomial coefficient can be nonpositive, equal -Delta/30 where Delta=e4-e3-5e2-10e1-45. Uniform cube sides have Delta(r)=r^4-4r^3-30r^2-40r-45, negative at 8 and positive at 9 with one positive root. The join volume is 24e4 by slice integration. If one side is 1, Delta(1,x,y,z)=-6(xy+xz+yz)-15(x+y+z)-55<0; hence sorted negative-witness sides 2<=a<=b<=c<=d. Candidate (7,8,8,11) has product 4928 and Delta=14. Any smaller/tied normalized volume obeys a^4<=4928, ab^3<=4928, abc^2<=4928, c<=d<=floor(4928/(abc)); exhaustive exact integer enumeration over exactly those proved bounds tests 10618 sorted tuples and finds only (7,8,8,11) with Delta>0. An independent loop in independent_checks.py reproduced the exhaustive result (not just the source verifier exit status). The pair-balancing identity follows from collecting the ab terms of Delta: Delta(a+1,b-1,c,d)-Delta(a,b,c,d)=(b-a-1)((c-1)(d-1)-6). This proves the entire integer family coefficient sign law and the finite exact minimum; the volume bound is essential to exhaustiveness.

## originality

PASS

Qualified PASS for the unique minimum normalized volume 118272 (side tuple 7,8,8,11), all-box positivity criterion and pair-balancing reversal. The classical join lattice-point convolution, eventually negative join examples and a large equal-cube witness are prior work; an elementary coefficient specialization is not the chief originality. The sharp four-parameter integer extremum and exact anisotropic minimizer are not obtained from general eventual nonpositivity in material inspected; historical orthotope tables might contain the exact tuple.

## value

PASS

The sharp first-volume counterexample in a natural, independently parameterized family strengthens a known asymptotic failure phenomenon into an exact finite threshold, with a rigorous computable exhaustive certificate. The closed symmetric-polynomial sign condition and complementary pair-balancing rule explain why the first witness is anisotropic, offering a useful benchmark for Ehrhart positivity under joins.

The dated certificate retains the supplied scientific assessment, sources and limitations.
