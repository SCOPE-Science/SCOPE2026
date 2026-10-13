# Exact two-support classification for the plus unitary-totient Lehmer equation
## Finding
Let \(\varphi^*(N)\) denote the unitary totient,
\[
\varphi^*(N)=\prod_{p^e\parallel N}(p^e-1),
\]
where the product runs over the exact prime-power blocks of \(N\). For integers \(N>1\) and \(M\ge1\) satisfying \(\omega(N)\le2\),
\[
M\varphi^*(N)=N+1
\]
holds if and only if
\[
(N,M)\in\{(2,3),(3,2),(15,2)\}.
\]
Thus \(15\) is the unique solution having exactly two distinct prime divisors.

## Assumptions and scope
Here \(\omega(N)\) is the number of distinct prime divisors of \(N\). The result is an exact classification for the first two prime-support layers; exponents are unrestricted. It does not claim a classification when \(\omega(N)\ge3\).

## Proof
First suppose \(\omega(N)=1\). Write \(N=A=p^a\). Then \(\varphi^*(N)=A-1\), so
\[
M(A-1)=A+1.
\]
Equivalently,
\[
(M-1)(A-1)=2.
\]
Since both factors are positive integers, the only possibilities are \((A-1,M-1)=(1,2)\) and \((2,1)\). Hence \((N,M)=(2,3)\) or \((3,2)\).

Now suppose \(\omega(N)=2\). Write
\[
N=AB,
\]
where \(A=p^a\) and \(B=q^b\) are prime powers with distinct prime bases. Put \(x=A-1\), \(y=B-1\), and \(k=M-1\). The defining equation is equivalent to
\[
(k+1)xy=(x+1)(y+1)+1,
\]
and therefore
\[
kxy=x+y+2. \tag{1}
\]
Because \(N+1>\varphi^*(N)\), any solution has \(M\ge2\), so \(k\ge1\).

If \(x=1\), then \(A=2\). The distinct prime base of \(B\) is odd, hence \(y=B-1\) is a positive even integer. Equation (1) becomes
\[
(k-1)y=3,
\]
which is impossible. The case \(y=1\) is symmetric.

It remains to consider \(x,y\ge2\). For such integers,
\[
2xy>x+y+2.
\]
Thus equation (1) rules out \(k\ge2\), and so \(k=1\). We obtain
\[
xy=x+y+2,
\]
or equivalently
\[
(x-1)(y-1)=3.
\]
Hence \(\{x,y\}=\{2,4\}\), so \(\{A,B\}=\{3,5\}\). Consequently \(N=15\) and \(M=2\).

Finally,
\[
\varphi^*(2)=1,\qquad \varphi^*(3)=2,\qquad \varphi^*(15)=8,
\]
so the three displayed pairs indeed satisfy the equation.

## Verification
The proof above is symbolic and has no search cutoff. The accompanying script `verify.py` independently evaluates \(\varphi^*(N)\) for every \(2\le N\le10^6\) having at most two distinct prime divisors and confirms that the only observed solutions are \((2,3)\), \((3,2)\), and \((15,2)\). This finite computation is regression evidence only; it is not used to prove the unbounded classification.

## Relationship to prior work
Yamada studies equations of the form \(M\varphi^*(N)=N\pm1\) and proves upper bounds for solutions under hypotheses beginning at larger prime support; the stated unitary-totient theorem does not classify the layers \(\omega(N)\le2\). Subbarao's classical unitary Lehmer problem concerns \(\varphi^*(N)\mid N-1\), not the plus equation here. Later unitary-Lehmer literature checked for comparison also formulates the unitary analogue with \(N-1\). The present result therefore isolates and completely resolves the natural first two support layers of the plus equation.

## Limitations
No assertion is made about existence, finiteness, or classification of solutions with \(\omega(N)\ge3\). The originality check covered the focal paper, the classical unitary-Lehmer formulation, representative later papers, the unitary-totient sequence and inverse table, and semantic searches; a remote possibility remains that an older source states the same low-support classification under different terminology.

## References
1. T. Yamada, “On Lehmer's problem and related problems,” arXiv:2303.16853, first submitted 2023-03-29; primary MSC 11A25.
2. M. V. Subbarao, “A companion to a Lehmer problem,” Publ. Math. Debrecen 52 (1998), 683–698.
3. “On Lehmer’s totient problem and its Unitary analogue,” PanAmerican Mathematical Journal 20 (2010), 21–35.
4. OEIS A047994, unitary totient function.
5. OEIS A361966, inverse unitary-totient counts/table.
