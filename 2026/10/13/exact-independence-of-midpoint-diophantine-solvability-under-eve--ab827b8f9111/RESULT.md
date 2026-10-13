# Exact independence of midpoint Diophantine solvability under even powering

## Finding

For coprime positive integers \(u,v\) with \(u\) odd and \(u\ge3\), write
\[
H(u,v)=\mathbf{1}\!\left\{\exists x,y\in\mathbb Z_{\ge0}:ux+vy=\frac{(u-1)(v-1)}2\right\}.
\]
Fix any odd integer \(a\ge3\), any nonempty finite set \(E\) of positive even integers, and \(L=\max E\). Regard \(b\) as a uniformly selected unit residue modulo \(a^L\), represented by an arbitrary positive coprime integer. Then \(H(a,b)\) is a fair binary variable and is **independent of the entire vector** \(\bigl(H(a^k,b^k)\bigr)_{k\in E}\). More precisely, for every binary vector \(\mathbf v\) indexed by \(E\),
\[
\#\{b\in(\mathbb Z/a^L\mathbb Z)^\times:H(a,b)=0,\ (H(a^k,b^k))_{k\in E}=\mathbf v\}
=\#\{b\in(\mathbb Z/a^L\mathbb Z)^\times:H(a,b)=1,\ (H(a^k,b^k))_{k\in E}=\mathbf v\}.
\]
Here membership depends only on the specified residue of \(b\).

For the square case, set
\[
S(a)=\#\left\{r\in\{1,\ldots,a-1\}:\gcd(r,a)=1,\ \text{the least positive residue of }r^2\pmod a\text{ is odd}\right\}.
\]
Among the \(a\varphi(a)\) unit classes modulo \(a^2\), the number satisfying \(H(a^2,b^2)=1\) is exactly
\[
Q(a)=\frac{a-1}{2}\varphi(a)+S(a).
\]
Consequently, for either \(\epsilon\in\{0,1\}\), the exact four-way table is
\[
\#\{b:H(a,b)=\epsilon,\ H(a^2,b^2)=1\}=\frac{Q(a)}2,
\qquad
\#\{b:H(a,b)=\epsilon,\ H(a^2,b^2)=0\}=\frac{a\varphi(a)-Q(a)}2.
\]
**Every one of the four patterns occurs in infinitely many positive coprime integers \(b\)** for each fixed odd \(a\ge3\). Each joint probability differs from \(1/4\) by at most \(1/(4a)\). When \(-1\) is a quadratic residue modulo \(a\), the four probabilities are exactly \(1/4\).

## Assumptions and scope

All powers have positive integer exponents. The parameter \(a\) is any fixed odd integer at least three; primality and squarefreeness are not assumed. The companion parameter \(b\) ranges over positive integers coprime to \(a\), including residue representatives chosen above \(a^L\) if a strict inequality \(b>a\) is desired. The count is finite and exact over a complete reduced residue system modulo \(a^L\); it also gives natural relative densities in the infinite set \(\{b\ge1:\gcd(a,b)=1\}\). The sign \(H\) denotes solvability of the displayed equation and does not assume any convention for other authors' signed notation.

## Proof

**Lemma (inverse parity).** For every odd integer \(u\ge3\) and positive integer \(v\) coprime to \(u\), let \(r\in\{1,\ldots,u-1\}\) be the inverse of \(v\) modulo \(u\). Then
\[
H(u,v)=1\quad\Longleftrightarrow\quad r\text{ is odd}.
\]
Indeed, put \(N=(u-1)(v-1)/2\). Any nonnegative solution \(ux+vy=N\) has \(0\le y<u\), since \(N<uv\). Reducing the equation modulo the odd number \(u\) gives
\[
2y\equiv r-1\pmod u.
\]
If \(r\) is odd, the unique candidate in \(0\le y<u\) is \(y=(r-1)/2\). Write \(vr=1+ut\) for an integer \(0\le t\le v-1\) (the upper bound follows from \(r<u\)); then
\[
2(N-vy)=(u-1)(v-1)-v(r-1)=u(v-1-t)\ge0.
\]
By the preceding congruence and oddness of \(u\), \(N-vy\) is a multiple of \(u\); it is nonnegative by the displayed identity, giving a solution. If \(r\) is even, the candidate is \(y=(u+r-1)/2\ge (u+1)/2\), which forces \(vy>v(u-1)/2>N\), so no solution exists. This also covers \(v=1\), when \(N=0\) and \(r=1\).

**Simultaneous independence.** Identify each \(b\) with its unit class modulo \(a^L\). Reflection \(b\mapsto-b\) is a fixed-point-free involution because \(a^L\) is odd and \(b\) is a unit. If \(r\) is the inverse of \(b\) modulo \(a\), the inverse of \(-b\) is \(a-r\). As \(a\) is odd, \(r\) and \(a-r\) have opposite parity; the lemma shows that the reflection interchanges \(H(a,b)=0\) and \(H(a,b)=1\). For any even \(k\in E\),
\[
(-b)^k\equiv b^k\pmod{a^k}.
\]
The lemma applied with \(u=a^k\) therefore shows that \(H(a^k,(-b)^k)=H(a^k,b^k)\). Hence each reflection pair contributes one instance of each value of \(H(a,b)\) while preserving the full even-power vector. This proves both the conditional count identity and the fair, independent law.

**Square marginal.** Invert \(b\) modulo \(a^2\), writing its inverse as \(w=r+at\) with \(r\in(\mathbb Z/a\mathbb Z)^\times\) represented in \(1,\ldots,a-1\) and \(t=0,\ldots,a-1\). The map \(b\mapsto w\) is a permutation of the units. For fixed \(r\),
\[
w^2\equiv r^2+2rat\pmod{a^2}.
\]
Since \(2r\) is invertible modulo the odd integer \(a\), these \(a\) squares occupy **every** lift of \(r^2\pmod a\) to a residue modulo \(a^2\), once each. Write \(s\) for the least positive residue of \(r^2\) modulo \(a\). The lifts are \(s,s+a,\ldots,s+(a-1)a\). Their parity alternates, so exactly \((a-1)/2+\mathbf1_{s\text{ odd}}\) are odd. By the inverse-parity lemma with \(u=a^2\), their oddness is precisely \(H(a^2,b^2)=1\). Summing over \(r\) proves \(Q(a)=(a-1)\varphi(a)/2+S(a)\); independence supplies the four-way counts.

Because \(0\le S(a)\le\varphi(a)\) and \(a\ge3\), both \(Q(a)\) and \(a\varphi(a)-Q(a)\) are strictly positive. The reflection count makes their halves positive integers. Repeating any relevant coprime residue class modulo \(a^2\) produces infinitely many positive \(b\) with its pair of decisions. The bound
\[
\left|\Pr(H(a,b)=\epsilon,H(a^2,b^2)=\eta)-\frac14\right|\le\frac1{4a}
\]
follows immediately by comparing \(Q(a)\) with \(a\varphi(a)/2\).

Finally, if \(t^2\equiv-1\pmod a\), multiplication \(r\mapsto tr\) permutes the units, taking \(r^2\pmod a\) to its negative. For odd \(a\), the least positive residues \(s\) and \(a-s\) have opposite parity. Therefore \(S(a)=\varphi(a)/2\), whence \(Q(a)=a\varphi(a)/2\) and all four counts equal \(a\varphi(a)/4\). No converse is asserted.

## Verification

The accompanying standalone `verify.py` uses only Python's standard library. It checks the inverse-parity lemma independently by direct enumeration of nonnegative Diophantine solutions for 1,387 coprime parameter pairs and checks the squared problem directly for 81 pairs. It exhausts all unit residue classes modulo \(a^2\) for the 30 odd integers \(3\le a\le61\), compares the exact four-way counts to the formula, and checks the involution for higher even powers and whole even-power vectors. Invoke `python3 verify.py` in the directory containing the included program. The provided `verify-output.txt` records one actual replay. These finite computations are corroboration, not a substitute for the proof for all odd \(a\).

For \(a=3\), the exact joint counts in order \((H(a,b),H(a^2,b^2))=(0,0),(0,1),(1,0),(1,1)\) are \(1,2,1,2\) over the six units modulo \(9\). For \(a=5\), all four counts equal \(5\) over the twenty units modulo \(25\).

## Relationship to prior work

Chu, Kim, Koch, Miller and Nguyen (2026, arXiv:2609.08728v1) revisit the paired midpoint equations and their behavior under squaring, proving relations for specified neighboring and congruence families. The available abstract and an indexed excerpt of its Section 4.3 describe the general squared-parameter relation as open; the full manuscript was not available for material inspection. The present result is **not** a general pointwise recovery rule. It supplies an exact conditional distribution, simultaneous independence for all even powers, and a square marginal, while showing that either unpowered solvability value coexists with both squared outcomes in every fixed odd-\(a\) family.

Binner's 2021 Theorem 4 (arXiv:2110.01558v1), inspected in the author's accessible full-text posting, gives an explicit description of representable and nonrepresentable integers for a fixed coprime pair. This broad pointwise membership theorem is compatible with the inverse-parity lemma; its inspected theorem and proof do not state the conditional counts over varying \(b\), simultaneous even-power independence, or the square-lifting marginal. The special distribution statements require the reflection pairing and uniform lift analysis above. Classical quadratic-residue parity identities may independently evaluate or bound \(S(a)\), and no novelty is claimed for those identities themselves.

## Limitations

The result requires the first parameter \(a\) to be odd and treats even powers. It does not determine pointwise \(H(a^2,b^2)\) from the single bit \(H(a,b)\); the exact four-pattern theorem demonstrates why no such single-bit rule can work. It does not classify every odd \(a\) for which \(S(a)=\varphi(a)/2\), and it makes no claim that all even-power vector patterns occur. The full 26-page motivating preprint could not be inspected through available access methods; a possible overlooked overlapping statement is a residual originality risk. No independent mathematical review has been performed.

## References

1. H. V. Chu, D. Kim, T. Koch, S. J. Miller, and A. V. Nguyen, *Generalizing a Pair of Diophantine Equations*, arXiv:2609.08728v1, first public 2026-09-08, https://arxiv.org/abs/2609.08728 .
2. D. S. Binner, *A Complete List of all Numbers not of the Form \(ax+by\)*, arXiv:2110.01558v1 (2021), https://arxiv.org/abs/2110.01558 ; author's full-text manuscript also accessible at https://www.researchgate.net/publication/355056186_A_Complete_List_of_all_Numbers_not_of_the_Form_axby .
