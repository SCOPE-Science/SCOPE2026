# The four symmetric consecutive-pentagonal semigroups with starting index at least two

## Finding
Let \(P_n=n(3n-1)/2\) denote the ordinary (noncentered) pentagonal number. For each integer \(n\ge2\), form the numerical semigroup
\[
 S_n=\langle P_n,P_{n+1},P_{n+2}\rangle
 =\{uP_n+vP_{n+1}+wP_{n+2}:u,v,w\in\mathbb Z_{\ge0}\}.
\]
Then \(S_n\) is symmetric **if and only if** \(n\in\{2,3,5,40\}\). Equivalently, precisely those four semigroup algebras are complete intersections. The two genuinely three-generated symmetric cases are
\[
 S_3=\langle12,22,35\rangle=\langle2\cdot6,2\cdot11,4\cdot6+11\rangle
\]
and
\[
 S_{40}=\langle2380,2501,2625\rangle
 =\langle35\cdot68,7\cdot68+27\cdot75,35\cdot75\rangle.
\]
The other two exceptional semigroups have embedding dimension two:
\(S_2=\langle5,12\rangle\) and \(S_5=\langle35,51\rangle\).

## Assumptions and scope
A numerical semigroup is an additive submonoid of the nonnegative integers with finite complement. It is symmetric if, writing \(F(S)\) for its greatest omitted integer, every integer \(z\) in the interval \(0\le z\le F(S)\) satisfies \(z\in S\) if and only if \(F(S)-z\notin S\). Equivalently its genus \(g(S)\), the number of omitted nonnegative integers, satisfies \(2g(S)=F(S)+1\). A numerical-semigroup algebra means \(k[t^s:s\in S]\) over an arbitrary field \(k\).

Throughout the claim \(n\) ranges over all integers at least two. The three displayed generators have greatest common divisor one: as proved below the common divisor of the first two divides two, whereas that of the first and third divides 35. Thus \(S_n\) really is a numerical semigroup. We use the classical characterization of symmetric three-generated semigroups (Herzog; explicit parameterization in Rosales and García-Sánchez, restated as Theorems 9–10 in García-Sánchez and Viola, 2015): for three **minimal** generators \(a,b,c\), symmetry holds exactly when some pair \(u,v\) has \(d=\gcd(u,v)>1\) and the remaining generator belongs to \(\langle u/d,v/d\rangle\). In this situation \(\gcd(d,w)=1\) follows from the total gcd-one condition. All two-generated numerical semigroups are symmetric.

## Proof
Write \(A=P_n\), \(B=P_{n+1}\), \(C=P_{n+2}\), so that
\[
 B-A=3n+1,\quad C-B=3n+4,\quad C-A=6n+5.
\]
Because \(\gcd(n,3n+1)=\gcd(n+1,3n+4)=1\), reduction of \(2A=n(3n-1)\) modulo \(3n+1\), and of \(2B=(n+1)(3n+2)\) modulo \(3n+4\), gives
\[
 \gcd(A,B)\mid2,\qquad \gcd(B,C)\mid2. \tag{1}
\]
Any \(d\mid\gcd(A,C)\) divides the odd integer \(6n+5\), and hence also \(2A=n(3n-1)\). Since
\[
 \gcd(n,6n+5)\mid5,\qquad
 \gcd(3n-1,6n+5)\mid7,
\]
we obtain
\[
 \gcd(A,C)\mid35. \tag{2}
\]
These two bounds imply \(\gcd(A,B,C)=1\).

For \(n\ge6\), \(C<2A\), because \(2A-C=(3n^2-13n-10)/2>0\). Accordingly \(A,B,C\) are all minimal generators: \(A<B<C<2A\). Direct inspection also gives minimality for \(n=3,4\). The two remaining cases are \(C=2A+B\) at \(n=2\), and \(C=2A\) at \(n=5\), both giving two-generator semigroups and hence symmetry.

Now assume \(n\ge71\). By (1), any nontrivial common divisor of the pair \((A,B)\) is two. If \(2C=xA+yB\), put \(s=x+y\). When \(s\le1\) the right side is at most \(B<2C\); when \(s\ge3\), it is at least \(3A>2C\), since
\[
 3A-2C=(3n^2-25n-20)/2>0 \quad(n\ge10).
\]
For \(s=2\), the right side is at most \(2B<2C\). So the third generator does not belong to \(\langle A/2,B/2\rangle\). Likewise a nontrivial common divisor of \((B,C)\) is two, and \(2A=xB+yC\) is impossible: if \(s\le1\), its right side is at most \(C<2A\), and if \(s\ge2\), its right side is at least \(2B>2A\). Thus neither adjacent pair gives a symmetric gluing.

For the remaining pair, let \(d=\gcd(A,C)>1\), so \(d\) is odd and \(d\le35\) by (2). A gluing would require integers \(x,y\ge0\) satisfying
\[
 dB=xA+yC. \tag{3}
\]
Set \(s=x+y\). At every \(n\ge71\), both inequalities
\[
 A>35(3n+1),\qquad C>35(3n+4) \tag{4}
\]
hold: after multiplying by two their left-minus-right differences are the increasing quadratics \(3n^2-211n-70\) and \(3n^2-199n-270\), both strictly positive at \(n=71\). If \(s\ge d+1\), then \(xA+yC\ge(d+1)A>dB\), by the first inequality in (4). If \(s\le d-1\), then \(xA+yC\le(d-1)C<dB\), by the second inequality. Therefore \(s=d\), and substituting \(x=d-y\) into (3) gives
\[
 y(6n+5)=d(3n+1),\qquad
 (2y-d)(6n+5)=-3d. \tag{5}
\]
Since \(d\) is odd, \(2y-d\) is a nonzero odd integer. Hence (5) implies \(6n+5\le3d\le105\), which is incompatible with \(n\ge71\). By the three-generator criterion no \(S_n\) for \(n\ge71\) is symmetric.

It remains to resolve the **complete finite interval** \(3\le n\le70\), excluding the redundant-generator case \(n=5\). The executable `verify.py` enumerates all three possible common-divisor pairs, computes the exact pair gcd \(d\), and tests the equivalent bounded Diophantine condition \(w=\alpha(u/d)+\beta(v/d)\) for all \(0\le\beta\le\lfloor w/(v/d)\rfloor\), with the uniquely determined \(\alpha\) checked for nonnegativity and integrality. Exhaustive integer division returns exactly \(n=3\) and \(n=40\), with the explicit representations shown above. This is a finite proof, not a sampling claim: the loop traverses every index in the only range left by the infinite argument and every feasible coefficient for every candidate pair. Together with the two redundant cases it gives precisely \(\{2,3,5,40\}\), as claimed.

## Verification
Running `python verify.py` requires only Python's standard library. The program asserts the four positive quadratic boundary values, the two redundant-generator identities, the two gluing representations, the complete finite list of gluing indices, and an **independent** Apéry-set computation of the Frobenius number and genus for every \(2\le n\le70\). In the latter check, a shortest-path algorithm finds the least semigroup element in each residue class modulo \(A\); if these least representatives are \(w_r\), then
\[
 F(S)=\max_r w_r-A,\qquad 2g(S)=\frac{2}{A}\sum_r w_r-(A-1).
\]
The independent criterion \(2g(S)=F(S)+1\) gives precisely the same indices. The four exceptional Frobenius numbers are respectively \(43,133,1699,258529\). The code is supplementary evidence for the finite step; it does not replace the symbolic proof for \(n\ge71\).

## Relationship to prior work
The OEIS entry A069757, publicly documented by May 16, 2003, concerns the *Frobenius numbers* of the exact same triple of ordinary pentagonal generators and tabulates initial values. It does not state a symmetry or complete-intersection classification. Theorem 10 in García-Sánchez and Viola (2015), tracing to Rosales and García-Sánchez (2009), supplies the general three-generator gluing criterion used above, but does not specialize it to pentagonal generators or produce the four-index classification. Lepilov, O'Rourke, and Swanson (2015) explicitly treat three consecutive **squares and cubes**, not pentagonal numbers. Fel's 2016 work treats powers with exponents two through four, not the quadratic pentagonal polynomial. The new content is the arithmetic restriction and its exceptional-index resolution for this previously tabulated natural family; it is not a new proof of the classical gluing theorem.

## Limitations
The conclusion concerns only ordinary pentagonal numbers at three consecutive positive indices with \(n\ge2\), not centered pentagonal numbers, higher-generator windows, or arbitrary quadratic figurate polynomials. This establishes symmetry and complete-intersection membership, not a closed formula for the Frobenius number or genus at general indices. The finite verification uses standard-library exact arithmetic. The literature comparison is based on the cited accessible sources and can miss unindexed or differently phrased prior work.

## References
1. OEIS Foundation, A069757, “Frobenius number of the numerical semigroup generated by three consecutive pentagonal numbers,” https://oeis.org/A069757 ; earliest visible public revision https://oeis.org/history?seq=A069757&start=10 (May 16, 2003).
2. P. A. García-Sánchez and C. Viola, “When the catenary degree agrees with the tame degree in numerical semigroups of embedding dimension three,” *Involve* 8 (2015), 677–694, Theorems 9–10, https://doi.org/10.2140/involve.2015.8.677 .
3. M. Lepilov, J. O'Rourke, and I. Swanson, “Frobenius numbers of numerical semigroups generated by three consecutive squares or cubes,” *Semigroup Forum* 91 (2015), 238–259, https://doi.org/10.1007/s00233-014-9687-8 .
4. L. G. Fel, “Numerical semigroups generated by squares, cubes and quartics of three consecutive integers” (2016), https://arxiv.org/abs/1608.08693 .
