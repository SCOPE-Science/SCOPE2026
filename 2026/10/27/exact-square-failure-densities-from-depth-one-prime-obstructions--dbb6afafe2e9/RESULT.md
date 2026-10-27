# Exact square-failure densities from depth-one prime obstructions

## Finding
Fix a positive integer \(h\) whose prime factors belong to one of these three classes: \(2\); odd primes congruent to \(3\pmod 4\); or primes congruent to \(13\) or \(17\pmod{20}\). For each positive integer \(x_0\), form
\[
x_{n+1}=\frac{h^2}{x_0+x_1+\cdots+x_n}=\frac{a_{n+1}}{b_{n+1}}
\]
with coprime positive integers \(a_{n+1},b_{n+1}\). Put \(Q_n=(2/h)a_n+b_n\), for \(n\ge2\). **Every \(Q_n\) for \(n\ge3\) is an integer square; only \(Q_2\) can fail.**

For each prime power \(p^a\parallel h\), define \(r_p=1\) for \(p=2\), \(r_p=2\) for \(p\equiv13,17\pmod{20}\), and \(r_p=0\) otherwise. Define the exact period
\[
M=\prod_{\substack{p^a\parallel h\\r_p>0}}p^{a+1},\qquad
N_0=\prod_{\substack{p^a\parallel h\\r_p>0}}(p^{a+1}-r_p),\qquad N_1=M-N_0.
\]
Empty products equal one. Among the \(M\) starting-value classes modulo \(M\), precisely \(N_0\) give no nonsquare term and \(N_1\) give exactly one. All classes with two or more failures are empty. Thus for positive starting values \(x_0\le X\), the proportions tend to \(N_0/M\) and \(N_1/M\), with counting errors \(O(M)\) for fixed \(h\).

In particular, \(h=221=13\cdot17\) has \(M=48841\), with \(47929\) classes giving zero failures and \(912\) giving one. The older general upper bound by the number of split prime factors can grow without bound, while the true bound on this infinite subfamily is always one.

## Assumptions and scope
Here \(h\) and \(x_0\) are arbitrary positive integers satisfying the stated prime-support restriction, with no squarefreeness assumption on \(h\). Every index \(n\ge2\) is included; perfect square means the square of a nonnegative integer, not merely a rational square. The density is natural density among the positive integers \(x_0\), for a fixed \(h\). The assertions are not made for \(h\) containing \(5\) or any prime \(p\equiv1,9\pmod{20}\).

## Proof
Write \(t_n=(x_0+\cdots+x_n)/h=u_n/v_n\) in lowest positive terms, so
\[
(u_0,v_0)=\left(\frac{x_0}{\gcd(x_0,h)},\frac h{\gcd(x_0,h)}\right),\quad
u_{n+1}=u_n^2+v_n^2,\quad v_{n+1}=u_nv_n.
\]
These pairs remain coprime. By Proposition 4.1 of [1], \(Q_{n+1}\) is an integer square exactly when \(\gcd(h,u_n)=1\), for every \(n\ge1\). For each prime divisor \(p\) of \(h\), the reduction of the homogeneous recursion defines
\[
T:\mathbb P^1(\mathbb F_p)\longrightarrow\mathbb P^1(\mathbb F_p),\quad [u:v]\longmapsto[u^2+v^2:uv].
\]
It sends \(0\) to \(\infty\) and fixes \(\infty\). A failure can therefore occur at \(Q_{n+1}\) only if the initial projective point reaches zero at exactly iteration \(n\ge1\).

For \(p\equiv3\pmod4\), the equation \(u^2+v^2=0\) has no nontrivial projective solution, so zero has no preimage. For \(p\equiv13,17\pmod{20}\), \(-1\) is a square modulo \(p\), and the only preimages of zero are \(\pm i\), where \(i^2=-1\). A preimage of either of these points would solve \(z^2\mp iz+1=0\), with discriminant \(i^2-4=-5\). Quadratic reciprocity gives \(\left(\frac{-5}{p}\right)=\left(\frac p5\right)=-1\) precisely in the stated two residue classes; neither quadratic has a root. Hence zero is reachable at iteration one only, never at a later iteration. For \(p=2\), the only preimage of zero is \(1\), and \(z^2+z+1\) has no root in \(\mathbb F_2\), giving the same one-level property. This proves that \(\gcd(h,u_n)=1\) for every \(n\ge2\), hence every \(Q_n\) for \(n\ge3\) is square.

It remains to count the \(x_0\) giving \(p\mid u_1=u_0^2+v_0^2\). Let \(p^a\parallel h\). If \(v_p(x_0)<a\), then \(p\nmid u_0\) and \(p\mid v_0\); if \(v_p(x_0)>a\), the opposite holds. Neither permits \(p\mid u_1\). If \(v_p(x_0)=a\), both are units, and the condition is
\[
\left(\frac{x_0/p^a}{h/p^a}\right)^2\equiv-1\pmod p.
\]
For each eligible odd prime there are exactly two solutions among the \(p^{a+1}\) classes of \(x_0\pmod{p^{a+1}}\). For \(p=2\) there is exactly one. Inert primes have no solutions. The Chinese remainder theorem multiplies the independent numbers of good classes, producing exactly \(N_0\) classes without a failure and \(M-N_0\) with one. Periodic counting gives the density formula and \(O(M)\) error. If at least one active prime divides \(h\), then \(0<N_1<M\), so both outcomes occur infinitely often, proving sharpness. \(\square\)

## Verification
The standalone `verify.py` enumerates initial points in \(\mathbb F_p\) for every eligible prime at most \(500\), checking one-level preimage rigidity; it also checks every initial residue class in a full period for \(h=1,3,13,17,26,39,169,221\) and tests the first several reduced homogeneous iterates. It prints `CERTIFICATE_OK` with the class counts, including \((N_0,N_1)=(47929,912)\) for \(h=221\) and \((501,175)\) for \(h=26\). All arithmetic is exact; these finite checks corroborate but do not replace the general proof.

## Relationship to prior work
Matijasevick, Rodríguez and Salazar [1] establish the coprime recurrence and exact criterion (Proposition 4.1), with the bound that each prime can spoil at most one index (Theorem B). Their Section 7, question (1), expressly asks for the proportions of starting values giving a prescribed number of failures. The present result solves that distribution problem for a specified infinite prime-support family, and strengthens the previous general bound to one irrespective of the number of eligible prime factors. No claim is made that the underlying recurrence or criterion is new.

## Limitations
The theorem is restricted to moduli with the specified prime support. It does not determine the distributions for primes \(5\) or \(p\equiv1,9\pmod{20}\), whose preimage trees can reach greater depth. An unpublished or unindexed equivalent treatment of this restricted family cannot be excluded. The argument invokes the exact square criterion of [1] rather than reproving every preliminary normalization lemma in that paper.

## References
[1] M. Matijasevick, S. Rodríguez, G. Salazar, *Perfect squares in reciprocal-sum sequences and primes that are inert in quadratic fields*, arXiv:2610.00765v1 (publicly posted 2026-09-30), especially Proposition 4.1, Remark 4.2 and Section 7 question (1). https://arxiv.org/html/2610.00765v1
[2] R. Jones and M. Manes, *Galois theory of quadratic rational functions*, Commentarii Mathematici Helvetici **89** (2014), 173–213 (general arithmetic-dynamical background; no attribution of the density formula).
