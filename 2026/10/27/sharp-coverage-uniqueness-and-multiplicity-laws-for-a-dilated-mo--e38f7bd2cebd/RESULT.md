# Exact singleton count for the Moser–de Bruijn coefficient-three sumset

## Finding

Let \(\mathcal M\) consist of the nonnegative integers with base-four digits in \(\{0,1\}\), and count ordered representations by
\[
r(n)=\#\{(a,b)\in\mathcal M^2:a+3b=n\}.
\]
For every integer \(k\ge0\), exactly \(3^k\) of the integers \(0\le n<4^k\) have \(r(n)=1\). In particular the proportion of uniquely represented integers among the represented integers in this interval tends to zero.

## Assumptions and scope

The two coefficient roles are distinct. Leading zeros do not create additional representations; zero has the single representation \((0,0)\). Only the coefficient three is considered. The count is for the intervals \([0,4^k)\), not arbitrary intervals of the same length.

## Proof

Set \(r(-1)=0\). The lowest digit pair contributes one of \(0,1,3,4\), each in exactly one way. Removing these digits gives, for \(m\ge0\),
\[
r(4m)=r(m)+r(m-1),\qquad r(4m+1)=r(4m+3)=r(m),\qquad r(4m+2)=0.
\]
In the residue-zero case the contribution 4 needs the remaining sum to be \(m-1\); all representations have a nonnegative remaining sum. These identities agree with the carry mechanism previously used in [1].

Write \(U_k\) for the desired count and let
\[
W_k=\#\{0\le m<4^k:r(m)+r(m-1)=1\}.
\]
The digit recurrence gives \(U_{k+1}=2U_k+W_k\). For the four adjacent-pair sums \(r(4m+d)+r(4m+d-1)\), in order of \(d=0,1,2,3\), write \(x=r(m)\) and \(y=r(m-1)\). The four sums are \(x+2y,2x+y,x,x\); for \(m=0\) the predecessor term is zero as required. For nonnegative integers \(x,y\), exactly one of \(x+2y,2x+y\) equals one when \(x+y=1\), and neither equals one otherwise. Summing over \(m\) therefore gives \(W_{k+1}=2U_k+W_k\) as well. Since \(U_0=W_0=1\), the two counts agree for every \(k\), and \(U_k=3^k\).

The earlier support theorem [1] gives \(((2+\sqrt2)^{k+1}+(2-\sqrt2)^{k+1})/4\) represented integers below \(4^k\). Dividing by this count shows that the unique proportion decays to zero, since \(3<2+\sqrt2\).

## Verification

Run `python3 verify.py` with Python 3. It constructs \(\mathcal M\cap[0,4^k)\) for \(0\le k\le7\), counts all relevant ordered pairs directly, and checks the singleton and adjacent-pair counts. This is finite corroboration; the proof treats every \(k\).

## Relationship to prior work and limitations

For coefficient two all integers have a unique representation, as can be seen by writing each base-four digit as \(\epsilon+2\delta\) with \(\epsilon,\delta\in\{0,1\}\). For coefficient three, [1] determined the support growth and Fibonacci maximum multiplicity; those are not claims of this result. The question addressed here is how many integers have exactly one representation, rather than whether they have any representation or how large their multiplicities can be. No assertion of exhaustive historical priority is made.

## Reference

[1] *A spectral counting law and Fibonacci multiplicities for the Moser–de Bruijn coefficient-three sumset*, published record `03c3bdcdf47a`, https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-a-spectral-counting-law-and-fibonacci-multiplicities-for-the-mos--03c3bdcdf47a .
