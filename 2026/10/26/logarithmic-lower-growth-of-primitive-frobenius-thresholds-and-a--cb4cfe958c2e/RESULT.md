# A primorial obstruction for primitive Frobenius numbers with one generator fixed

## Finding

For coprime integers \(a,b\ge2\), let \(g(a,b)\) be the largest nonnegative integer with no representation \(ax+by\) by nonnegative integers \(x,y\) satisfying \(\gcd(x,y)=1\). Finiteness follows from Jaffe [1, Theorem 4.3].

For integers \(a\ge3\) and \(R\ge2\), set
\[
Q_a(R)=\prod_{\substack{p\le R\\p\text{ prime},\ p\nmid a}}p.
\]
If \(b>aQ_a(R)\) and \(\gcd(a,b)=1\), there is a nonnegative integer \(n\) with \(Rb<n<(R+1)b\) that has no primitive representation. In particular, \(g(a,b)>Rb\). For each fixed \(a\ge3\), this gives
\[
\liminf_{\substack{b\to\infty\\\gcd(a,b)=1}} \frac{g(a,b)}{b\log b}\ge1.
\]

## Assumptions and scope

The multipliers are nonnegative, not necessarily positive. A representation is primitive only if the multipliers are relatively prime. The empty prime product is \(1\); \(R\) is an integer and there is no primality condition on \(b\). Logarithms are natural. Only the finite assertion allows \(a\) to vary freely.

## Proof

Put \(Q=Q_a(R)\). The residue \(-b\) modulo \(a\) is a unit distinct from \(b\): equality would imply \(a\mid2\), since \(\gcd(a,b)=1\). The Chinese remainder theorem gives a unique class modulo \(aQ\) with
\[
n\equiv0\pmod Q,\qquad n\equiv-b\pmod a.
\]
Its smallest representative strictly above \(Rb\) lies in \((Rb,Rb+aQ]\subset(Rb,(R+1)b)\).

For any nonnegative representation \(n=ax+by\), reducing modulo \(a\) gives \(y\equiv-1\pmod a\). Hence \(y\ge a-1\ge2\) and \(\gcd(y,a)=1\). The upper bound \(n<(R+1)b\) gives \(y\le R\). If \(R<a-1\), no such \(y\) exists. Otherwise let \(p\) be any prime divisor of \(y\). Then \(p\le R\) and \(p\nmid a\), so \(p\mid Q\mid n\). Since \(p\mid by\) and \(p\nmid a\), the equation forces \(p\mid x\). This proves that every nonnegative representation is nonprimitive, including a possible representation with \(x=0\).

Fix \(a\ge3\) and \(0<\varepsilon<1\). The prime number theorem gives \(\log Q_a(R)=R+o(R)\), since the sum of \(\log p\) over the omitted primes dividing \(a\) is bounded independently of \(R\). For \(R=\lfloor(1-\varepsilon)\log b\rfloor\) and sufficiently large \(b\), this yields \(\log(aQ_a(R))<\log b\). The finite bound gives \(g(a,b)>Rb\) for every such coprime \(b\). Divide by \(b\log b\), take the liminf, and let \(\varepsilon\downarrow0\).

## Verification

The witness can be replayed by solving the two congruences and taking the smallest representative greater than \(Rb\). For example, \((a,R,b)=(3,2,7)\) gives \(Q=2\), witness \(20\), and the only nonnegative representation has \((x,y)=(2,2)\). The empty-product case \((a,R,b)=(4,2,5)\) gives \(Q=1\), witness \(11\), and no nonnegative representation. These are checks of the finite construction; the general lower bound uses the proof and prime number theorem, not finite data.

## Relationship to prior work

Ding, Wang and Zhang [2, Theorem 1.7] give a logarithmic lower bound along a subsequence of second coefficients. A limsup lower bound leaves open whether the same growth holds for every sufficiently large coprime second coefficient. The finite witness above applies to every \(b\) above the stated threshold, giving a liminf bound with leading lower constant one. For contrast, the exact formula \(g(2,b)=4b-2\) for odd \(b\ge3\) is prior work [2, Theorem 1.8; 1, Proposition 5.2] and is not part of the finding.

The joint-growth obstruction in [3] requires \(\min(a,b)\) to exceed a growing primorial, so its asymptotic does not cover fixed \(a\). The distinct catalogue entry [4] states the same liminf conclusion with a related finite witness in a different interval, under different parameter conditions. The shared asymptotic is an exact overlap; no independent priority is asserted.

## Limitations

The lower bound does not establish optimality of the constant, a matching upper bound, or uniformity of the asymptotic for growing \(a\).

## References

1. G. N. Jaffe, *Denominators in the Farey Sequence, the Stern Sequence, and the Frobenius Problem with Relatively Prime Multipliers*, [arXiv:2610.17267](https://arxiv.org/abs/2610.17267), Theorem 4.3 and Proposition 5.2.
2. Y. Ding, W. Wang, and H. Zhang, *The Diophantine Frobenius Problem revisited*, [arXiv:2509.08599](https://arxiv.org/abs/2509.08599), Theorems 1.7 and 1.8.
3. *Uniform primorial obstructions for primitive two-generator Frobenius numbers*, [indexed finding](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-uniform-primorial-obstructions-for-primitive-two-generator-frobe--0eee43f23b58/RESULT.md).
4. *Primorial obstructions force \(b\log b\) growth for primitive Frobenius numbers*, [indexed finding](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-primorial-obstructions-force-b-log-b-growth-for-primitive-froben--d4c334da51d4/RESULT.md).
