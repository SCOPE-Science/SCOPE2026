# Positive density of odd nonsquare non-signed-perfect abundant integers

## Finding

An integer \(n\) is \(\{-1,1\}\)-perfect if one can choose a sign \(\epsilon_d\in\{-1,1\}\) for every proper divisor \(d>1\) such that
\[
n=1+\sum_{1<d<n,\ d\mid n}\epsilon_d d.
\]
As usual, \(\sigma(n)\) is the sum of all positive divisors and \(n\) is abundant if \(\sigma(n)>2n\).

**Theorem.** Fix an odd square \(a\) with \(\sigma(a)>2a\), and set \(C=\sigma(a)\). For any integer
\[
Y>\max\{C+1,P^+(2a)\},
\qquad
\rho_Y=\prod_{p\le Y}\left(1-\frac1p\right),
\]
where \(P^+(u)\) is the largest prime dividing \(u\), the odd nonsquare abundant multiples of \(a\) which are not \(\{-1,1\}\)-perfect have lower natural density at least
\[
\boxed{\frac{\rho_Y}{a}\left(1-\frac{C+1}{Y}\right)>0.}
\]
Consequently, the odd nonsquare abundant integers that are not \(\{-1,1\}\)-perfect form a set of **positive lower natural density**.

For example, choose
\[
a=11025=3^2\cdot5^2\cdot7^2,
\qquad C=13\cdot31\cdot57=22971,
\qquad Y=50000.
\]
This yields the explicit positive lower bound
\[
\frac1{11025}\left(1-\frac{22972}{50000}\right)
\prod_{p\le50000}\left(1-\frac1p\right).
\]

## Assumptions and scope

All densities are measured among positive integers \(n\le X\), divided by \(X\); the density statement is a \(\liminf\), not an assertion that the relevant natural density exists. The theorem holds for **every** fixed odd abundant square, with a possibly different admissible \(Y\). No primality or squarefreeness hypothesis is placed on the cofactor \(m\), only coprimality, a small divisor-sum excess, and nonsquareness; these will hold on a set of positive lower density.

The fixed-source benchmark is the problem studied in John M. Campbell, *Disproofs of two conjectures concerning nondeficient numbers* (arXiv:2607.11043v1, 2026). The signed-perfect definition originates in Tyler Ross, *A Perfect Number Generalization and Some Euclid–Euler Type Results* (2024).

## Proof

**Step 1: an interval obstruction.** For odd \(a\) which is a square, \(C=\sigma(a)\) is odd. Write
\[
C-2a=2h+1>0,
\qquad h\in\mathbb Z_{\ge0}.
\]
Let \(m>1\) be odd, nonsquare, coprime to \(a\), and satisfy
\[
s(m):=\sigma(m)-m<\frac mC.
\]
Put \(n=am\) and \(b=Cs(m)<m\). Since \(a\) and \(m\) are coprime, \(\sigma(n)=C\sigma(m)>2am\). Thus \(n\) is odd and abundant. Because \(a\) is a square, \(n\) is nonsquare exactly when \(m\) is nonsquare.

The signed-perfect condition is equivalent to demanding that
\[
H:=\frac{\sigma(n)-2n}{2}
\]
be a sum of distinct proper divisors of \(n\) greater than \(1\): change the signs of precisely those divisors. Here
\[
H=\frac{(C-2a)m+Cs(m)}2
=hm+\frac{m+b}2.
\]
As \(b<m\), one has
\[
hm+b<H<(h+1)m.
\]
Any subset of proper divisors \(d>1\) of \(n=am\) has a sum of the form \(Am+B\), where \(A\) is the sum of the selected divisors divisible by \(m\) after removing the factor \(m\), hence a nonnegative integer. All remaining divisors have the form \(uv\), with \(u\mid a\) and \(v\mid m\), \(v<m\). Their total contribution satisfies
\[
0\le B\le\sigma(a)(\sigma(m)-m)=b.
\]
If \(A\le h\), then \(Am+B\le hm+b<H\). If \(A\ge h+1\), then \(Am+B\ge(h+1)m>H\). Neither can equal \(H\). Therefore \(n=am\) is **not** \(\{-1,1\}\)-perfect.

**Step 2: an explicit positive-density supply of cofactors.** Fix the stated integer \(Y\) and set
\[
Q_Y=\prod_{p\le Y}p,
\qquad
R_Y=\{m\ge1:\gcd(m,Q_Y)=1\}.
\]
The set \(R_Y\) has natural density \(\rho_Y>0\). In particular, all its members are odd and coprime to \(a\). Define the nonnegative weight
\[
G_Y(m)=\sum_{\substack{p\mid m\\p>Y}}\frac1{p-1}.
\]
For every \(m\in R_Y\), the Euler product for \(\sigma(m)/m\) and the inequality \(-\log(1-1/p)\le1/(p-1)\) give
\[
\log\frac{\sigma(m)}m\le G_Y(m).
\]
Also \(\log(1+1/C)>1/(C+1)\). Hence
\[
G_Y(m)<\frac1{C+1}
\quad\Longrightarrow\quad
\sigma(m)-m<\frac mC.
\]

We now bound the average of \(G_Y\) rigorously. Since \(Q_Y\) is fixed, for each prime \(p>Y\), counting coprime residue classes modulo \(Q_Y\) gives
\[
\#\{m\le X:(m,Q_Y)=1,\ p\mid m\}
=\rho_Y\frac Xp+O(Q_Y).
\]
Summing with weight \(1/(p-1)\) over \(Y<p\le X\) yields
\[
\sum_{\substack{m\le X\\m\in R_Y}}G_Y(m)
=\rho_Y X\sum_{Y<p\le X}\frac1{p(p-1)}+O_Y(\log X)
\le \frac{\rho_Y X}{Y}+o_Y(X).
\]
The last inequality uses only the telescoping elementary bound
\[
\sum_{p>Y}\frac1{p(p-1)}
\le\sum_{k>Y}\frac1{k(k-1)}=\frac1Y.
\]
By Markov's counting inequality, the members of \(R_Y\cap[1,X]\) for which \(G_Y(m)\ge1/(C+1)\) number at most
\[
\frac{\rho_Y(C+1)}Y X+o_Y(X).
\]
Thus at least
\[
\rho_Y\left(1-\frac{C+1}{Y}\right)X+o_Y(X)
\]
members satisfy \(\sigma(m)-m<m/C\). Deleting perfect squares removes only \(O(\sqrt X)\) candidates, so the same positive lower-density bound holds for nonsquare \(m\). All remaining \(n=am\) are qualifying counterexamples by Step 1. Scaling the count by \(a\) establishes the asserted lower bound among integers \(n\).

## Verification

The attached `artifacts/verify.py` uses exact arithmetic to check the anchor \(a=11025\), the oddness and positivity of its divisor-sum gap, the admissibility of \(Y=50000\), and both inequalities defining the obstruction interval on prime and composite sample cofactors. It also computes the finite Euler product for the displayed quantitative lower bound. The complete proof of the density assertion is the preceding averaging argument, not finite enumeration or a numerical extrapolation.

## Relationship to prior work

Ross's 2024 Conjecture 17 proposed that every odd nonsquare abundant integer is \(\{-1,1\}\)-perfect. Campbell's 2026 paper refutes it in two distinct ways: Section 2 gives a **positive-density family of even** counterexamples, while Section 3 gives an **infinite sparse family of odd nonsquare** counterexamples with prime cofactors \(m=p\). In particular, an infinite prime family does not imply positive natural density, and an even positive-density family does not imply an odd one. The present theorem combines a general fixed odd abundant-square obstruction with an elementary explicit density sieve for nonsquare, not-necessarily-prime cofactors and thus yields a strictly stronger qualitative conclusion for the odd nonsquare class.

The searchable preprint was inspected through its full-text public mirror; its definitions, key density lemma, main theorems and both appendices were compared as mathematical statements. No published proof of an odd nonsquare positive-density lower bound was found in the checked sources.

## Limitations

The bound is explicit but not optimized. No upper density, existence of the natural density, asymptotic exact constant, or characterization of all odd nonsquare counterexamples is claimed. The proof presupposes the standard multiplicativity of \(\sigma\) on coprime inputs and uses no prime number theorem. The publisher edition was not fully accessible, although the full version-1 preprint was inspected through a public full-text mirror; this is a residual coverage risk rather than a claim of exhaustive literature uniqueness.

## References

1. John M. Campbell, *Disproofs of two conjectures concerning nondeficient numbers*, arXiv:2607.11043v1 (first posted 2026-07-13), especially Sections 2–3, Lemmas 2.1–2.3 and Theorems 2.4 and 3.1. https://arxiv.org/abs/2607.11043
2. Tyler Ross, *A Perfect Number Generalization and Some Euclid–Euler Type Results*, Journal of Integer Sequences **27** (2024), Article 24.7.5, especially Conjecture 17. https://cs.uwaterloo.ca/journals/JIS/VOL27/Ross/ross3.pdf
