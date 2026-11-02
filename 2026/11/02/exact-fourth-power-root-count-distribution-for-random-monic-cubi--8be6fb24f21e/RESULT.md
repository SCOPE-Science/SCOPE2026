# Exact fourth-power root-count distribution for random monic cubics

## Finding

Let \(p\ge3\) be an odd prime. Choose the three coefficients of a monic cubic \(f(X)=X^3+aX^2+bX+c\) independently uniformly from \(\mathbb Z/p^4\mathbb Z\). Let \(R_p(f)\) be the number of **distinct residue classes** \(x\bmod p^4\) with \(f(x)\equiv0\pmod{p^4}\). Set

\[
B_0=\frac{p^3-p}{3},\quad B_1=\frac{p^2(p-1)}2,\quad
B_2=p(p-1),\quad B_3=\binom p3,
\]

and \(n_0=B_0\), \(n_1=B_1+p\), \(n_2=B_2\), \(n_3=B_3\). Define the two probability polynomials

\[
D_p(z)=1-\frac{p-1}{2p^2}-\frac1{p^3}
+\frac{p-1}{2p^2}z^{2p}+\frac{z^{p^2}}{p^3}
\]

and

\[
T_p(z)=1-\frac{p-1}{p^2}-\frac{n_1+n_2+n_3}{p^6}
+\frac{p-1}{p^2}z^p
+\frac{n_1z^{p^2}+n_2z^{2p^2}+n_3z^{3p^2}}{p^6}.
\]

Then the **complete** probability generating function is

\[
\boxed{\mathbb E[z^{R_p(f)}]
=\frac{B_0+B_1z+B_3z^3+B_2zD_p(z)+pT_p(z)}{p^3}.}
\]

In particular, the possible root counts for \(p\ge5\) are exactly
\(0,1,3,p,2p+1,p^2,p^2+1,2p^2,3p^2\); when \(p=3\), the values \(3\) and \(p\) coincide and their masses add. The sharp maximum is \(3p^2\). Exactly \(p^4\binom p3\) of the \(p^{12}\) monic cubics attain it, so

\[
\boxed{\Pr(R_p(f)=3p^2)=\binom p3/p^8.}
\]

All maximizing cubics are precisely those for which a unique \(t\bmod p\) exists such that the translated coefficients in
\(f(t+Y)=Y^3+AY^2+BY+C\) satisfy \(p\mid A\), \(p^2\mid B\), \(p^3\mid C\), and the monic cubic
\(Y^3+(A/p)Y^2+(B/p^2)Y+C/p^3\) splits into three **distinct** linear factors modulo \(p\). The quotients are read modulo \(p\), and \(A,B,C\) are represented by integers modulo \(p^4\); the divisibility requirements and the splitting property are independent of the chosen lift of \(t\), although the three reduced coefficients can change under a translation of \(t\) by \(p\). The residue \(t\) is unique because the original reduction is \((X-t)^3\).

## Assumptions and scope

All probabilities are over the exactly \(p^{12}\) coefficient triples of monic cubics modulo \(p^4\). The variable \(z\) is formal. Only odd primes \(p\ge3\) are asserted; no claim is made for \(p=2\), higher degree, higher prime-power exponent, or distribution of true \(p\)-adic roots. Root multiplicity is not counted: one residue root counts once regardless of multiplicity. The prime-power exponent is exactly four.

## Proof

**1. Classification of reduction types.** A monic cubic over \(\mathbb F_p\) has five disjoint factorization classes: irreducible cubic (\(B_0\) polynomials, no roots); a single linear factor times an irreducible quadratic (\(B_1\), one simple root); three distinct linear factors (\(B_3\), three simple roots); a double linear factor and a different simple linear factor (\(B_2\), one double plus one simple); and a triple linear factor (\(p\) choices). The counts follow by selecting the linear roots and, for \(B_0\), using the degree-three irreducible count \((p^3-p)/3\). Their sum is \(p^3\). Every simple root lifts uniquely modulo \(p^4\) by the simple-root Hensel lemma, and no root exists over a residue that is not already a root mod \(p\). It remains to determine the double and triple branches. Coefficient lifts are uniform independently conditional on their reduction type.

**2. Double-root branch.** Translate the double root to \(0\): write \(f(t+Y)=Y^3+AY^2+BY+C\), with \(p\nmid A\), \(p\mid B\), \(p\mid C\). A root over this residue is \(x=t+py\), \(y\bmod p^3\), and

\[
f(t+py)=C+pBy+p^2Ay^2+p^3y^3.
\]

If \(p^2\nmid C\), no such root exists. This has probability \(1-1/p\). If \(p^2\mid C\), divide by \(p^2\): the condition is
\[
H(y)=C/p^2+(B/p)y+Ay^2+py^3\equiv0\pmod{p^2}.
\]

The discriminant of the reduced quadratic \(H\bmod p\) is uniform in \(\mathbb F_p\) (its constant term is independently uniform). For odd \(p\), its discriminant is a nonzero square with probability \((p-1)/(2p)\), a nonsquare with the same probability, and zero with probability \(1/p\). A nonzero-square discriminant gives two simple roots modulo \(p\), exactly two roots \(y\bmod p^2\), and thus \(2p\) roots \(x\bmod p^4\). A nonsquare gives none. In the zero-discriminant case there is one double reduced root \(y_0\). All \(p\) lifts \(y_0+pu\bmod p^2\) solve \(H\equiv0\pmod{p^2}\) exactly when \(H(y_0)\equiv0\pmod{p^2}\). An independent next coefficient digit makes this event probability \(1/p\), giving \(p^2\) roots \(x\bmod p^4\), or none otherwise. Multiplying the conditional probabilities proves the polynomial \(D_p(z)\). The other, simple, residue root adds one, hence contributes \(zD_p(z)\).

**3. Triple-root branch.** Translate the unique reduced root to \(0\). Now \(p\mid A,B,C\) and the same expansion holds. If \(p^2\nmid C\), no roots lift. If \(p^2\mid C\) but \(p^2\nmid B\), division by \(p^2\) gives a linear polynomial in \(y\) modulo \(p\) with nonzero derivative. It has one root modulo \(p^2\), hence exactly \(p\) roots \(x\bmod p^4\). This occurs with probability \((p-1)/p^2\). If \(p^2\mid B\) but \(p^3\nmid C\), there are no roots. Finally, \(p^2\mid B\) and \(p^3\mid C\) occur with probability \(p^{-3}\). In this event

\[
f(t+py)\equiv p^3 G(y)\pmod{p^4},\qquad
G(y)=y^3+(A/p)y^2+(B/p^2)y+C/p^3\pmod p.
\]

The coefficients of \(G\) are independent uniform elements of \(\mathbb F_p\), since they occupy distinct, unconstrained base-\(p\) digits of the translated coefficients. Each root \(y\bmod p\) of \(G\) corresponds to exactly \(p^2\) distinct \(x\bmod p^4\). The counts of finite-field monic cubics with exactly \(0,1,2,3\) distinct roots are, respectively,
\[
n_0=(p^3-p)/3,\quad n_1=p^2(p-1)/2+p,\quad n_2=p(p-1),\quad n_3=\binom p3.
\]

Indeed, the single-root case includes a triple linear factor (\(p\) choices), whereas the two-root case is a double factor times another simple factor. Consequently the nonzero triple-branch masses are \((p-1)/p^2\) at \(R=p\) and \(n_j/p^6\) at \(R=jp^2\), \(j=1,2,3\); all remaining mass is at \(0\). This is \(T_p(z)\).

**4. Combination and extreme event.** The five reduction classes occur with probabilities \(B_0/p^3\), \(B_1/p^3\), \(B_3/p^3\), \(B_2/p^3\), and \(p/p^3\), respectively. Averaging their conditional root-count generating functions gives the boxed formula. Because \(p\ge3\), the triple-branch value \(3p^2\) strictly exceeds all other possible counts. Attaining it is equivalent to the divisibility conditions in the statement together with three distinct roots of \(G\). There are \(p\) possibilities for the translated residue \(t\); for each, the three constrained translated coefficients produce every monic \(G\bmod p\) equally often, with exactly \(p^3\) lifts per \(G\); and exactly \(\binom p3\) monic cubics \(G\) split into three distinct linear factors. Thus the number of maximizing coefficient triples is \(p\cdot p^3\binom p3=p^4\binom p3\), completing the proof.

## Verification

Compile and run `verify.cpp` using `g++ -std=c++17 -O3 -Wall -Wextra verify.cpp -o verify && ./verify`. The program independently enumerates all \(3^{12}=531441\) monic cubics modulo \(3^4=81\), counts every root by direct substitution, checks the exact extremizer classification for each polynomial, and checks sharpness witnesses for \(p=5,7,11\). The exhaustively observed histogram for \(p=3\) is

\[
\{0:201852,\;1:277749,\;3:32805,\;7:13122,\;9:972,\;10:4374,\;18:486,\;27:81\}.
\]

The included `verify_distribution.py` checks exact rational coefficients at seven primes and reproduces all eight counts exactly at \(p=3\); its coefficient sum is \(531441\) and its weighted first moment is also \(531441\), as required by uniformity of the constant coefficient. The verification exhausts one prime only, and the theorem for all odd primes is established by the proof.

## Relationship to prior work

Nir's 2026 work on deterministic integer-root algorithms develops weighted lifting trees for repeated modular roots and bounds the number of branches; its Section 5 does not evaluate the random cubic distribution modulo \(p^4\). Cheng, Gao, Rojas and Wan (2017/2019) develop a general root-counting algorithm for arbitrary polynomials modulo \(p^t\); Section 4 treats the fourth power, including a pointwise \(p^2\)-times-finite-field counting formula for a branching case. Their theorem is an important antecedent, but it neither gives the coefficient-averaged generating function nor evaluates all five reduction classes for uniformly random monic cubics. Jain (2024/2026) gives the expectation over general finite rings and full distributions over fields, not the finite-ring cubic law. Caruso (2021) studies actual \(p\)-adic roots and moments, which do not identify the number of temporary roots modulo \(p^4\). A related computation of the complete distribution modulo \(p^3\) does not determine the next-level conditional double- and triple-branch laws used here.

## Limitations

No priority claim is made against uninspected historical work or unpublished calculations. An equivalent probability law might already be known under a different language. This is a finite-level modular theorem, not a description of actual \(p\)-adic roots or of all levels \(p^k\). The case \(p=2\) has different finite-field root statistics and is not included. Self-review is not independent mathematical auditing.

## References

1. Itamar Nir, *Faster Deterministic Integer Root Finding for Integer Polynomials*, arXiv:2608.00668 (first posted 2026-08-01), especially Section 5 on lifting trees. https://arxiv.org/abs/2608.00668
2. Qi Cheng, Shuhong Gao, J. Maurice Rojas, and Daqing Wan, *Counting Roots of Polynomials Over Prime Power Rings*, arXiv:1711.01355 (2017), published in Open Book Series 2 (2019), especially Sections 2 and 4. https://arxiv.org/html/1711.01355v1
3. Ritik Jain, *The number of solutions of a random system of polynomials over a finite field*, arXiv:2409.06866 (2024; revised 2026), especially Theorems 1 and 2. https://arxiv.org/html/2409.06866v2
4. Xavier Caruso, *Where are the zeroes of a random p-adic polynomial?*, arXiv:2110.03942 (2021). https://arxiv.org/html/2110.03942v1
