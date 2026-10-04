# No even perfect number is a sum of two positive \(m\)-th powers when \(m\equiv1\pmod4\)

## Finding
Let
\[
m\ge5,\qquad m\equiv1\pmod4.
\]
Then no even perfect number can be written as
\[
N=x^m+y^m
\]
with positive integers \(x,y\).

Thus the Gallardo--Zelinsky conjecture that \(28\) is the only even perfect number expressible as a sum of two equal positive powers is proved for the entire exponent class
\[
m\equiv1\pmod4.
\]
In particular, the previously unresolved first case \(m=5\) is impossible.

## Assumptions and scope
By the Euclid--Euler theorem, every even perfect number has the form
\[
N=2^{p-1}(2^p-1),
\]
where \(p\) and \(M=2^p-1\) are prime.

Suppose for contradiction that
\[
2^{p-1}M=x^m+y^m
\]
for positive integers \(x,y\) and \(m=4k+1\ge5\). Write
\[
t=\min\{\nu_2(x),\nu_2(y)\},\qquad x=2^t u,\qquad y=2^t v,
\]
so \(u,v\) are positive and not both even. Then
\[
2^{p-1-mt}M=u^m+v^m.
\]
The equality itself implies \(mt\le p-1\).

The proof below uses only this standard even-perfect-number form and elementary congruences.

## Proof
Factor
\[
u^m+v^m=(u+v)B_m(u,v),
\]
where
\[
B_m(u,v)
=
u^{m-1}-u^{m-2}v+u^{m-3}v^2-\cdots-uv^{m-2}+v^{m-1}.
\]

First suppose that \(u,v\) have opposite parity. Then \(u+v\) and \(B_m(u,v)\) are both odd. Also
\[
u+v\ge3.
\]
Moreover \(B_m(u,v)>1\), since otherwise
\[
u^m+v^m=u+v,
\]
which for positive \(u,v\) and \(m\ge2\) can occur only at \(u=v=1\), contrary to opposite parity. Hence the odd part of \(u^m+v^m\) is a product of two integers exceeding \(1\). But the odd part of the left side is the single prime \(M\), appearing to the first power. This is impossible.

Therefore \(u,v\) are both odd. Then \(B_m(u,v)\) is odd. If \(B_m(u,v)=1\), again
\[
u^m+v^m=u+v
\]
forces \(u=v=1\), making the right side \(2\), impossible because it has no odd prime factor \(M\). Hence \(B_m(u,v)>1\).

Since the odd part of
\[
2^{p-1-mt}M
\]
is exactly the prime \(M\), the factorization
\[
(u+v)B_m(u,v)
\]
with \(u+v\) even and \(B_m(u,v)\) odd forces
\[
B_m(u,v)=M.
\]

Now reduce \(B_m(u,v)\) modulo \(8\). Because \(u,v\) are odd, \(v\) is invertible modulo \(8\). Put
\[
r\equiv uv^{-1}\pmod8.
\]
Every odd residue satisfies
\[
r^2\equiv1\pmod8.
\]
Since \(m=4k+1\),
\[
B_m(u,v)
\equiv
r^{4k}-r^{4k-1}+\cdots-r+1
\pmod8,
\]
because \(v^{m-1}\equiv1\pmod8\).

There are \(2k+1\) even powers of \(r\), each congruent to \(1\), and \(2k\) odd powers, each congruent to \(r\). Therefore
\[
B_m(u,v)\equiv (2k+1)-2kr
=1+2k(1-r)\pmod8.
\]
For
\[
r\in\{1,3,5,7\},
\]
this residue is always either
\[
1\quad\text{or}\quad5\pmod8.
\]
Thus
\[
B_m(u,v)\not\equiv7\pmod8.
\]

If \(p\ge3\), however,
\[
M=2^p-1\equiv7\pmod8,
\]
contradicting \(B_m(u,v)=M\).

The remaining Euclid--Euler parameter is \(p=2\), for which \(N=6\). But for \(m\ge5\), either \(x=y=1\), giving \(x^m+y^m=2\), or one of \(x,y\) is at least \(2\), giving
\[
x^m+y^m\ge2^m+1\ge33.
\]
So \(6\) is impossible as well.

Hence no even perfect number is a sum of two positive \(m\)-th powers for any
\[
m\ge5,\qquad m\equiv1\pmod4.
\]

## Verification
The proof is symbolic and covers every exponent in the stated congruence class.

The accompanying `verify.py` independently checks the only finite residue calculation used in the proof. For all odd residues \(u,v\pmod8\) and all representatives
\[
m\equiv1\pmod4
\]
through a broad finite range, it evaluates the alternating factor directly and confirms that its residue is always \(1\) or \(5\), never \(7\). It also checks the closed formula
\[
B_m(u,v)\equiv1+2k(1-r)\pmod8.
\]
This computation is a regression check only; the infinite residue argument is proved above.

## Relationship to prior work
Gallardo and Zelinsky formulate the conjecture that if an even perfect number is a sum
\[
x^m+y^m
\]
with positive integers and \(m\ge2\), then necessarily \(m=3\) and the perfect number is \(28\). They note that the cubic case is known and that even exponents are already excluded.

Their paper then discusses the first remaining odd case \(m=5\) and explicitly says that their method appears insufficient even there. The argument above settles not only \(m=5\) but every exponent
\[
m\equiv1\pmod4.
\]

Targeted searches using the source title, authors, the exact \(m=5\) case, the congruence class \(m\equiv1\pmod4\), and the equation for even perfect numbers did not locate a prior statement of this infinite exponent-class result. Broader searches for sums of two odd powers and even perfect numbers likewise did not locate a covering theorem.

## Limitations
The proof does not address odd exponents
\[
m\equiv3\pmod4
\]
beyond the already-known cubic case. Thus it does not prove the full Gallardo--Zelinsky conjecture.

The originality search cannot rule out an unindexed or otherwise difficult-to-locate observation. The mathematical proof itself does not depend on the searches.

## References
1. Luis H. Gallardo and Joshua Zelinsky, “A Note on a Result of Makowski,” arXiv:2310.07077, first posted 10 October 2023; later published in *Elemente der Mathematik*, DOI 10.4171/EM/558.
