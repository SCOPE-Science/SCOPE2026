# Even-base squarefree digit-sum collisions of positive density

## Finding
For any integer base \(b\ge12\), let \(S_b(n)\) be the sum of the base-\(b\) digits of the positive integer \(n\), and define \(H_b(n)=nS_b(n)\). Put
\[
Q=b^2-2,\qquad U=2b-1,\qquad V=2b-3,\qquad X=UQ,\qquad Y=VQ.
\]
For **every even** \(b\ge12\) satisfying \(b\not\equiv4\pmod7\) and the squarefreeness of \(Q,U,V\), the distinct positive integers \(X,Y\) are squarefree and obey
\[
H_b(X)=H_b(Y)=(2b-1)(2b-3)(b^2-2).
\]
The set \(\mathcal B\) of even bases satisfying these conditions has the following **exact positive natural density among all positive integers**:
\[
\boxed{\displaystyle
\delta(\mathcal B)=\frac12\cdot\frac79\cdot\frac{40}{49}
\prod_{\substack{p\ge5\ \mathrm{prime}\\p\ne7}}
\left(1-\frac{3+\left(\frac2p\right)}{p^2}\right)>0,}
\]
where \(\left(\frac2p\right)\) is the Legendre symbol. Numerically the product is approximately \(0.2696\). In particular, the digit-sum product is noninjective on squarefree positive integers for a positive-density family of **even bases** exceeding \(10\).

## Assumptions and scope
The only ambient assumptions are that the base is a positive even integer at least \(12\), together with the specified modular and squarefreeness conditions. The density counts bases, not arguments to the digit-sum function. No claim is made that every even base satisfies the hypotheses or that the noninjectivity question is resolved for all bases.

## Proof
The exact base-\(b\) expansions, with each displayed digit between \(0\) and \(b-1\), are
\[
X=(1,\ b-2,\ b-4,\ 2)_b,
\qquad
Y=(1,\ b-4,\ b-4,\ 6)_b.
\]
Indeed both expansions simplify to \((2b-1)(b^2-2)\) and \((2b-3)(b^2-2)\), respectively. Since \(b\ge12\), all digits are legitimate. Therefore \(S_b(X)=2b-3=V\) and \(S_b(Y)=2b-1=U\). Multiplication gives \(H_b(X)=UVQ=H_b(Y)\), while \(X-Y=2Q>0\).

We next prove squarefreeness. For all integers \(b\),
\[
(2b-1)(2b+1)-4(b^2-2)=7,\qquad
4(b^2-2)-(2b-3)(2b+3)=1.
\]
Thus \(\gcd(Q,U)\mid7\) and \(\gcd(Q,V)=1\). Also \(\gcd(U,V)=1\), since both are odd and differ by \(2\). The factor \(7\) divides both \(Q\) and \(U\) exactly when \(b\equiv4\pmod7\). The exclusion of this congruence class makes \(Q,U,V\) pairwise coprime. Hence their assumed squarefreeness makes \(X=UQ\) and \(Y=VQ\) squarefree.

For the density, sieve by prime squares. At \(p=2\), exactly half of the residue classes are even; for them \(Q\equiv2\pmod4\) and \(U,V\) are odd, so no further local exclusion occurs. This gives \(1/2\). At \(p=3\), \(b^2-2\) has no root modulo \(3\), whereas \(U,V\) each have one distinct root modulo \(9\), giving \(7/9\).

At \(p=7\), the restriction \(b\not\equiv4\pmod7\) removes seven residue classes modulo \(49\). Of the other classes, the unique lift modulo \(49\) of the root \(b\equiv3\pmod7\) of \(Q\) and the unique root of \(V\) modulo \(49\) each remove one additional class. These are disjoint, so \(40\) of the \(49\) classes survive.

For any odd prime \(p\ge5\), \(p\ne7\), the two linear factors \(U,V\) have two distinct roots modulo \(p^2\). The quadratic \(Q\) has exactly two roots modulo \(p^2\) when \(2\) is a quadratic residue modulo \(p\), and none otherwise. Hensel's elementary simple-root lifting applies because every root of \(Q\) has nonzero derivative \(2b\) modulo \(p\). The gcd identities above ensure that these sets of roots are disjoint. Therefore the number of forbidden classes is \(3+\left(\frac2p\right)\), as stated in the Euler product.

For any fixed cutoff \(P\), the Chinese remainder theorem gives the product of these local fractions as the density of bases obeying the restrictions for primes at most \(P\). To pass to all primes, consider bases \(12\le b\le T\). Any additional violation requires a prime \(p>P\) with \(p^2\) dividing one of \(Q,U,V\). Such a prime is at most \(T\) for \(T\ge12\). For each odd \(p\) there are at most four relevant residue classes modulo \(p^2\), hence at most \(4(T/p^2+1)\) such bases. Their total count is bounded by
\[
4T\sum_{p>P}\frac1{p^2}+4\pi(T)=o_P(T)+4T\sum_{p>P}\frac1{p^2},
\]
using the standard estimate \(\pi(T)=o(T)\). As \(P\to\infty\), the normalized upper bound tends to zero. Thus the full natural density exists and equals the displayed Euler product. It is positive because every local factor is positive and the series of their deviations from \(1\) converges. This completes the proof.

## Verification
The standalone standard-library Python program `verifier.py` verifies the base-digit expansions and collision identity for all even \(12\le b\le1000\), checks independent squarefreeness for \(12\le b\le400\), and exhaustively counts the local residue classes modulo \(p^2\) for every prime \(p\le101\). It also computes a truncated Euler product, which is **not** an infinite-product certificate. Run `python3 verifier.py` in the directory containing the extracted file. The proof above, not finite enumeration, establishes the unrestricted theorem and density.

For \(b=12\), \(Q=142\), \(U=23\), \(V=21\), so \(X=3266\), \(Y=2982\), and \(H_{12}(3266)=H_{12}(2982)=68586\); both inputs are squarefree.

## Relationship to prior work
Noppakaew and Pongsriiam, *Product of Some Polynomials and Arithmetic Functions* (Journal of Integer Sequences 26 (2023), Article 23.9.1), define \(H_b\) in Example 11. Example 14 proves squarefree noninjectivity for bases \(2\) through \(10\), and Question 30 asks about all bases \(b\ge11\). The present theorem gives a positive-density family of **even** bases through a different, quadratic-factor collision and additionally computes its exact density. The unrestricted question remains open.

## Limitations
The formula does not determine noninjectivity for every even base, every odd base, or every base at least \(11\); it provides an explicit infinite family of witnesses with exact density. The standalone numerical computation supplements the proof but does not establish infinite squarefreeness or any general theorem on its own. Equivalent formulations not captured by the inspected literature remain a bibliographic possibility.

## References
1. P. Noppakaew and P. Pongsriiam, *Product of Some Polynomials and Arithmetic Functions*, Journal of Integer Sequences **26** (2023), Article 23.9.1, https://cs.uwaterloo.ca/journals/JIS/VOL26/Pongsriiam/pong43.pdf (especially Examples 11 and 14 and Question 30).
2. Same article's bibliographic entry and publication date: https://cs.uwaterloo.ca/journals/JIS/VOL26/Pongsriiam/pong43.html (published November 2, 2023).
