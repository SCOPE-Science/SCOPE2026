# Exact even-window cube-sum GCDs for Fibonacci and Lucas numbers

## Finding

Let the Fibonacci and Lucas sequences be defined for all integer indices by \(F_0=0\), \(F_1=1\), \(L_0=2\), \(L_1=1\), and the recurrence \(X_{j+2}=X_{j+1}+X_j\). For every positive integer \(k\) and every nonnegative integer \(n\), set
\[
S_X(n;k)=\sum_{i=1}^{k}X_{n+i}^{3},\qquad G_X(k)=\gcd\{S_X(n;k):n\geq0\},\quad X\in\{F,L\}.
\]
For **every integer \(m\geq1\)**, the exact even-window GCDs are
\[
\boxed{G_F(2m)=2^{-\mathbf1_{3\mid m}}3^{\mathbf1_{4\mid m}}\begin{cases}F_m,&2\mid m,\\ L_m,&2\nmid m,\end{cases}}
\]
and
\[
\boxed{G_L(2m)=5^{\mathbf1_{2\mid m}}G_F(2m).}
\]
Equivalently, in a form with only ordinary integer GCDs,
\[
G_F(2m)=\begin{cases}\dfrac{F_m}{2}\gcd(F_m^2-3,6),&2\mid m,\\[4pt]\dfrac{L_m}{2}\gcd(L_m^2-15,6),&2\nmid m,\end{cases}
\]
\[
G_L(2m)=\begin{cases}\dfrac{5F_m}{2}\gcd(F_m^2-3,6),&2\mid m,\\[4pt]\dfrac{L_m}{2}\gcd(L_m^2-15,6),&2\nmid m.\end{cases}
\]
All displayed values are integers. These formulas provide a closed answer for the even-window cubic case raised by Mbirika and Spilker (Question 6.1 in the cited paper).

## Assumptions and scope

All indices are integers unless otherwise stated. The GCD is the positive greatest common divisor of an infinite set of positive integers; only \(m\geq1\), \(n\geq0\), and even lengths \(k=2m\) are asserted. Extend the sequences to negative indices by \(F_{-j}=(-1)^{j+1}F_j\) and \(L_{-j}=(-1)^jL_j\). Write \(\mathbf1_P\) for the indicator of a true proposition \(P\).

## Proof

**1. Two universal integer templates.** Put
\[
E_X(z)=X_{3z}+X_{3z-3},\quad D_X(z)=X_{z-1}-X_z,
\]
\[
B_z(t)=tE_L(z)-12(-1)^zD_L(z),\qquad C_z(t)=tE_F(z)+12(-1)^zD_F(z).
\]
The step-three subsequences \(F_{3z},L_{3z}\) obey the characteristic polynomial \(T^2-4T-1\); the signed subsequences \((-1)^zF_z,(-1)^zL_z\) obey \(T^2+T-1\). Therefore each of \(B_z(t)\) and \(C_z(t)\), for fixed integer \(t\), satisfies the fourth-order integer recurrence with characteristic polynomial
\[
P(T)=(T^2-4T-1)(T^2+T-1)=T^4-3T^3-6T^2+3T+1.
\]
The constant coefficient is \(1\), so the recurrence works both forward and backward over the integers. Hence the GCD of values over any tail \(z\geq z_0\) equals the GCD of any four consecutive values, in particular those at \(z=0,1,2,3\).

Direct substitution at these four indices gives the **complete** integer-linear certificates
\[
\begin{aligned}
(B_0,B_1,B_2,B_3)&=(36-2t,\;6t+12,\;22t+24,\;94t-12),\\
(C_0,C_1,C_2,C_3)&=(2t+12,\;2t+12,\;10t,\;42t+12).
\end{aligned}
\]
Consequently,
\[
\begin{aligned}
\gcd_{z\geq z_0}B_z(t)
&=2\gcd(t-18,\;3(t+2),\;11t+12,\;47t-6)\\
&=2\gcd(t-18,60,210,840)=2\gcd(t-18,30),\\
\gcd_{z\geq z_0}C_z(t)
&=2\gcd(t+6,5t,21t+6)\\
&=2\gcd(t+6,30,120)=2\gcd(t+6,30).
\end{aligned}
\]
For the first equality, the remaining three entries reduce modulo \(t-18\) to \(60,210,840\). For the second, they reduce modulo \(t+6\) to \(-30,-120\). Absolute values are implicit in GCD notation.

**2. Cubic identities and telescoping.** The standard triple-angle identities are
\[
5F_j^3=F_{3j}-3(-1)^jF_j,\qquad L_j^3=L_{3j}+3(-1)^jL_j.
\]
For either \(X=F\) or \(X=L\), the signed sequence \(Y_j=(-1)^jX_j\) obeys \(Y_{j+2}=-Y_{j+1}+Y_j\), while \(Z_j=X_{3j}\) obeys \(Z_{j+2}=4Z_{j+1}+Z_j\). Thus, whenever \(b\geq a\),
\[
\sum_{j=a}^bY_j=-\bigl(Y_{b+1}+Y_b-Y_a-Y_{a-1}\bigr),\quad
4\sum_{j=a}^bZ_j=Z_{b+1}+Z_b-Z_a-Z_{a-1}.
\]
Set \(a=n+1\), \(b=n+2m\), and \(z=a+m\). The classical addition formulas imply
\[
\begin{array}{c|cc}
& m\ \mathrm{even}&m\ \mathrm{odd}\\ \hline
F_{r+2m}-F_r&F_mL_{r+m}&L_mF_{r+m}\\
L_{r+2m}-L_r&5F_mF_{r+m}&L_mL_{r+m}
\end{array}
\]
for all integer \(r\). Apply these to the two telescoped sums with step \(2m\) and \(6m\). Use \(F_{3m}=F_m(5F_m^2+3)\) when \(m\) is even and \(L_{3m}=L_m(L_m^2+3)\) when \(m\) is odd. Exact simplification yields all four identities
\[
\begin{array}{c|c|c}
& m\ \mathrm{even}&m\ \mathrm{odd}\\ \hline
F&20S_F(n;2m)=F_m B_z(5F_m^2+3)&20S_F(n;2m)=L_m C_z(L_m^2+3)\\
L&4S_L(n;2m)=5F_m C_z(5F_m^2+3)&4S_L(n;2m)=L_m B_z(L_m^2+3).
\end{array}
\]
These are exact integer identities for **every** \(n\geq0\), not congruences or finite observations.

**3. Take the GCD of every shift.** By Step 1 and the four identities, if \(m\) is even,
\[
\begin{aligned}
20G_F(2m)&=2F_m\gcd(5F_m^2-15,30),\\
4G_L(2m)&=10F_m\gcd(5F_m^2+9,30).
\end{aligned}
\]
The first inner GCD is \(5\gcd(F_m^2-3,6)\). The second is \(\gcd(F_m^2-3,6)\), since \(5F_m^2+9\) is prime to \(5\) and is congruent to \(-(F_m^2-3)\) modulo \(6\). This proves both even-\(m\) cases.

If \(m\) is odd,
\[
\begin{aligned}
20G_F(2m)&=2L_m\gcd(L_m^2+9,30),\\
4G_L(2m)&=2L_m\gcd(L_m^2-15,30).
\end{aligned}
\]
The identity \(L_m^2-5F_m^2=4(-1)^m\) gives \(L_m^2\equiv1\pmod5\) for odd \(m\). Therefore
\[
\gcd(L_m^2+9,30)=5\gcd(L_m^2-15,6),\quad
\gcd(L_m^2-15,30)=\gcd(L_m^2-15,6).
\]
This proves both odd-\(m\) cases.

**4. Reduce to the sharp divisibility indicators.** The elementary periods modulo \(2\) and \(3\) give
\[
2\mid F_m\ \Longleftrightarrow\ 3\mid m,\quad
2\mid L_m\ \Longleftrightarrow\ 3\mid m,\quad
3\mid F_m\ \Longleftrightarrow\ 4\mid m,
\]
and \(3\nmid L_m\) for odd \(m\). Accordingly,
\[
\gcd(F_m^2-3,6)=2^{\mathbf1_{3\nmid m}}3^{\mathbf1_{4\mid m}}\quad(m\ \mathrm{even}),
\]
\[
\gcd(L_m^2-15,6)=2^{\mathbf1_{3\nmid m}}\quad(m\ \mathrm{odd}).
\]
Substitution establishes the two boxed formulas and completes the proof.

## Verification

The standalone, standard-library-only script `verify.py` recomputes both sequences, checks the four exact factorization identities for \(1\leq m\leq80\) and \(0\leq n\leq7\), checks the predicted GCDs against independently calculated four-shift GCDs, verifies the exact four-value templates, and tests the unimodular recurrence. These finite computations test implementation and boundary cases; the universal proof is Steps 1–4.

## Relationship to prior work

Mbirika and Spilker, *GCD of sums of \(k\) consecutive squares of generalized Fibonacci numbers* (first public preprint 26 April 2022, arXiv:2204.12626, Question 6.1), establish square-sum GCDs and explicitly raise the cubic and higher-power cases. The even-length cube formulas displayed there are conjectural and do not match the all-shift GCDs in small instances: for example, at \(k=6\) the actual Fibonacci cubic GCD is \(2\) rather than the conjecturally displayed \(4\). The result above gives complete even-length values for both standard sequences. Adegoke, *Factored closed-form expressions for the sums of cubes of Fibonacci and Lucas numbers* (arXiv:1706.08469), provides identities for sparse even-index subsequences, not GCDs over every translate of consecutive cubes. Guyer and Mbirika (arXiv:2104.12262) give GCDs for first powers, not cubes. Known recurrence theory explains why four shifts suffice, but does not by itself provide the evaluated factors \(2\), \(3\), and \(5\).

## Limitations

Only even window lengths and the ordinary Fibonacci and Lucas initial conditions are classified here. No assertion is made for odd lengths or arbitrary generalized Fibonacci initial data. Computational tests are not a proof. Literature and database searches cannot exclude inaccessible, implicit, or unindexed earlier derivations; independent mathematical and publication-priority review has not been carried out.

## References

1. aBa Mbirika and Jürgen Spilker, *GCD of sums of \(k\) consecutive squares of generalized Fibonacci numbers*, arXiv:2204.12626v2 (first submitted 2022-04-26), especially Question 6.1, pp. 13–14. https://arxiv.org/abs/2204.12626
2. Kunle Adegoke, *Factored closed-form expressions for the sums of cubes of Fibonacci and Lucas numbers*, arXiv:1706.08469v2 (2017), especially the introduction and identities (1.5)–(1.8). https://arxiv.org/abs/1706.08469
3. Dan Guyer and aBa Mbirika, *GCD of sums of \(k\) consecutive Fibonacci, Lucas, and generalized Fibonacci numbers*, arXiv:2104.12262 (2021). https://arxiv.org/abs/2104.12262
