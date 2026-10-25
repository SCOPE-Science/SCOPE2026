# Exact universality-index law for height-three Dyck words

## Finding
For \(n,k\ge0\), let \(a_{n,k}\) be the number of Dyck words of length \(2n\), nesting height at most three, and fixed-binary-alphabet scattered-subsequence universality index \(k\). Then
\[
F(z,u)=\sum_{n,k\ge0}a_{n,k}z^nu^k=
\frac{1-4uz+(u+4u^2)z^2+(u-3u^2)z^3}
{(1-uz)((1-2uz)^2-u^2z^3)}.
\]
For uniform choice among these words at semilength \(n\), the random index \(K_n\) obeys
\[
\frac{K_n}{n}\xrightarrow{\mathbb P}\frac2{\sqrt5},\qquad
\lim_{n\to\infty}\frac{\mathbb E K_n}{n}=\frac2{\sqrt5}.
\]
In particular, \(F(z,1)=(1-2z)/(1-3z+z^2)\). The first index-count rows for \(n=1,2,3,4\) are respectively \(u\), \(u+u^2\), \(u+3u^2+u^3\), and \(5u^2+7u^3+u^4\).

## Assumptions and scope
A Dyck word uses \(0\) as an opening step and \(1\) as a closing step: each prefix has at least as many zeros as ones, the final totals agree, and height is the largest prefix excess. A word has index \(k\) if every binary word of length \(k\) is a scattered subsequence and this fails at length \(k+1\). The alphabet is fixed as \(\{0,1\}\), even for the empty word, whose index is zero. The restriction is *global maximum height at most three*, not a condition comparing heights of successive first-return components. All variables are formal; the limit statements concern uniform finite sets at a fixed semilength.

## Proof
**Greedy arches.** A complete binary arch is the shortest nonempty prefix of the remaining word containing both letters. A repeated decomposition into complete arches and a final incomplete remainder counts the universality index, by the arch-factorization criterion [2]. In binary, an arch starts at some position and ends at the first subsequent occurrence of its opposite symbol. Equivalently, after reading a symbol, greedily select the earliest adjacent unlike pair not sharing a position with the previously selected pair. Every selected pair completes one arch, and no incomplete trailing run does so. Thus a two-state flag suffices: a letter at the previous position was used in a selected pair or was not.

**Twelve-state transfer.** Excluding the empty word, the first step must be \(0\). Let \(h\in\{0,1,2,3\}\) be the current height, \(b\in\{0,1\}\) the last letter, and \(m\in\{0,1\}\) the flag that the last letter was already paired. The reachable states are all \((h,b,m)\) satisfying \(b=1\) at \(h=0\), \(b=0\) at \(h=3\), and arbitrary \(b,m\) at the other heights. There are exactly twelve. If a next bit \(c\) gives height \(h'=h+1\) for \(c=0\), or \(h'=h-1\) for \(c=1\), retain the step only if \(0\le h'\le3\). Set
\[
m'=\mathbf1_{\{c\ne b,\ m=0\}},
\]
and give the step weight \(x u^{m'}\). Start after one letter in state \((1,0,0)\), with prefactor \(x\), and accept exactly the states having \(h=0\). With \(A(x,u)\) the resulting \(12\)-square weighted transition matrix, \(e\) the coordinate of \((1,0,0)\), and \(t\) the indicator column of accepting states, this defines
\[
G(x,u)=1+x e^{\mathsf T}(I-A(x,u))^{-1}t.
\]
The inverse is a valid formal series because \(A(0,u)=0\). Every accepted path is a Dyck word, its exponent of \(u\) equals its number of completed arches, and it has even length; hence \(G(x,u)=F(x^2,u)\).

**Exact rational identity.** Put \(z=x^2\),
\[
N(z,u)=1-4uz+(u+4u^2)z^2+(u-3u^2)z^3,
\]
\[
D(z,u)=(1-uz)((1-2uz)^2-u^2z^3)
=1-5uz+8u^2z^2-(u^2+4u^3)z^3+u^3z^4.
\]
The identity \(G(x,u)D(x^2,u)=N(x^2,u)\) follows by exact finite polynomial verification. Indeed, the rational transfer expression has numerator and denominator degrees at most twelve in \(x\), because both are a determinant of a twelve-square matrix (the numerator arises from a single bordered determinant). Consequently the numerator of the difference between the transfer expression and \(N/D\), after cross-multiplication, has degree at most twenty in \(x\). Both denominators have constant coefficient one, so it suffices to prove equality of formal coefficients through \(x^{20}\). The standalone verifier enumerates all twelve-state transition paths symbolically in \(u\), constructs the coefficients at every even length through twenty (the odd coefficients are identically zero by parity), and verifies \(D F=N\) as an identity in \(\mathbb Z[u]\) through \(z^{10}\). This proves that the numerator polynomial vanishes identically, not merely that a finite list of experimental counts agrees.

**Asymptotics.** At \(u=1\), cancellation gives
\[
F(z,1)=\frac{1-2z}{1-3z+z^2}.
\]
Its unique smallest-modulus singularity is the simple positive root \(\rho=(3-\sqrt5)/2\). For \(u\) near one the unique nearby dominant pole \(\rho(u)\) is the analytic simple root of \(H(z,u)=(1-2uz)^2-u^2z^3\), and its numerator does not cancel. Standard simple-pole coefficient expansion, uniform in \(u\) around one, yields \([z^n]F(z,u)=C(u)\rho(u)^{-n}(1+O(q^n))\) for some \(q<1\) and analytic nonzero \(C\). Logarithmic differentiation of the normalized probability generating polynomial shows
\[
\mathbb E K_n=-n\frac{\rho'(1)}{\rho(1)}+O(1),\qquad
\operatorname{Var}K_n=O(n).
\]
Implicit differentiation of \(H(\rho(u),u)=0\) gives \(-\rho'(1)/\rho(1)=2/\sqrt5\). The variance bound and Chebyshev's inequality prove convergence in probability.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter. It constructs the twelve allowed states from the stated height/flag rules, checks the exact polynomial identity through degree twenty in \(x\), then independently enumerates all height-at-most-three Dyck words through semilength ten and compares the complete index histogram. For semilength at most eight it additionally checks directly whether every subsequence of the claimed length exists and at least one of the next length is absent. Its success terminates with `HEIGHT3_DYCK_ARCH_DISTRIBUTION_PASS`. The bounded symbolic degree argument above turns the polynomial-identity check into a certificate of the all-length generating function. Finite word enumeration alone does not prove the theorem.

## Relationship to prior work
Hébrard's arch criterion, as developed by Schnoebelen and Veron [2], supplies the universality-index mechanism. Mol, Rampersad, and Shallit [1] study Dyck words with nesting restrictions, particularly in pattern avoidance and automatic sequences, without giving this joint index distribution. Baril, Genestier, and Kirgizov [3] analyze consecutive-pattern statistics in a *different* class of Dyck paths whose first-return decomposition satisfies an ordering condition on heights; their restriction is not the uniform global height cutoff here. Previously available extremal height/index relationships determine minimum possible indices but not the complete distribution or typical index. The present claim is restricted to the exact height bound three, not all finite height bounds.

## Limitations
The probability limit is conditional on global Dyck height at most three; it does not apply to uniformly random unrestricted Catalan Dyck words. The result does not identify a full limiting central-limit distribution or a formula at arbitrary height. The novelty assessment remains subject to potentially equivalent, differently indexed transfer-matrix enumerations; no independent mathematical audit has been completed.

## References
[1] L. Mol, N. Rampersad, J. Shallit, *Dyck Words, Pattern Avoidance, and Automatic Sequences*, arXiv:2301.06145 (first public January 15, 2023), https://arxiv.org/abs/2301.06145 .

[2] P. Schnoebelen, J. Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:2304.11932 (April 24, 2023), https://arxiv.org/abs/2304.11932 .

[3] J.-L. Baril, R. Genestier, S. Kirgizov, *Pattern distributions in Dyck paths with a first return decomposition constrained by height*, arXiv:1911.03119 (first public November 8, 2019), https://arxiv.org/abs/1911.03119 .
