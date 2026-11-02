# Independent mathematical audit

## correctness

PASS

From open-neighborhood votes on two-row rook R_n=K_2 square K_n, row update g(U,V) equals empty, V, or full according to a=|U|<k,=k,>k for even n=2k; for odd n=2k+1 it is empty, V\U, U^c union V, or full for a<k,=k,=k+1,>k+1. Exhaustive 16 row-population type cases (plus intersection sizes) prove eventual primitive period at most 2, exact recurrent/fixed counts and depths at most 2 (even), at most 3 (odd >=5). With B=binom(n,k), L=sum_{j<k}binom(n,j), even n: fixed 4+B, primitive-two states B^2-B, depth counts D0=4+B^2,D1=4L^2+4B-4,D2=4B(L-1). Odd n: fixed 4, primitive-two states 2(k+2)B, D0=4+2(k+2)B, D1=A-D0,D2=4^n-A-H,D3=H with A=4L^2+2B(2^{k+1}+(k+1)^2), H=4 sum_{a=1}^{k-1} a binom(n,a)binom(n-a,k). Independently computed individual vertex votes, cycles and exact distributions across all 21,824 labelled states for n=3..7.

## originality

PASS

The classic symmetric-threshold theorem provides eventual periods at most 2; Kaaser--Mallmann-Trenn--Natale bounds convergence on general graphs. Neither inspected source supplies the exact two-row rook period-type distribution or parity-dependent transient census. The previously studied complementary crown dynamics is expressly prior: its odd-n total recurrent count equals the new rook count but the fixed/two-cycle splitting is opposite.

## value

PASS

Classifying the complete attractor and transient spectrum of a natural highly symmetric graph family is meaningful in deterministic voting dynamics. The sharp parity-dependent depth and counterintuitive crown-versus-rook inversion are structural phenomena beyond a general period-two bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
