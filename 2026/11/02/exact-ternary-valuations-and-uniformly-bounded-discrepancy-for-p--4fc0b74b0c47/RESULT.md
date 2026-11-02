# Exact ternary valuations and uniformly bounded discrepancy for Perrin numbers

## Finding

Let \(R_0=3\), \(R_1=0\), \(R_2=2\), and \(R_{n+3}=R_{n+1}+R_n\) be the classical Perrin numbers. For every index \(n\ge2\), write \(n=13m+r\), where \(0\le r<13\). Three effectively determined elements \(\beta_1,\beta_3,\beta_9\in\mathbb Z_3\) yield the complete valuation law

\[
\nu_3(R_n)=
\begin{cases}
0,&r\notin\{0,1,3,9\},\
1,&r=0,\
1+\nu_3(m-\beta_r),&r\in\{1,3,9\}.
\end{cases}
\]

Here \(\beta_1=0\), \(\beta_3\equiv4477\pmod{6561}\), and \(\beta_9\equiv2107\pmod{6561}\). The only zero of the nonnegative-index Perrin sequence is \(R_1=0\). The roots are uniquely specified by the congruences

\[
R_{13m+r}\equiv0\pmod{3^{j+1}},\qquad
m\equiv\beta_r\pmod{3^j}\quad(j\ge1).
\]

Define \(C_t(N)=\#\{2\le n<N:\nu_3(R_n)=t\}\). For all nonnegative integers \(t,N\),

\[
\left|C_t(N)-p_t N\right|\le 9,
\qquad
p_t=\begin{cases}
9/13,&t=0,\
3/13,&t=1,\
6/(13\cdot3^t),&t\ge2.
\end{cases}
\]

Thus every nonnegative ternary valuation occurs with positive natural density, and all levels have an error bounded independently of the level and cutoff.

## Assumptions and scope

The theorem concerns the **unshifted classical** Perrin sequence, not Padovan numbers or shifted Perrin values. Define \(\nu_3(a)\) as the exponent of \(3\) dividing a nonzero integer \(a\), and use \(\nu_3(0)=+\infty\) when discussing \(R_1\). The same valuation on \(\mathbb Z_3\) is used for the roots. The count excludes the initial zero index \(n=1\) and starts at \(n=2\). All congruences and matrices in the proof are exact integer identities, and every stated bound applies to arbitrary cutoffs, not just powers of three.

## Proof

**1. Companion matrix and thirteen-step return.** Put

\[
M=\begin{pmatrix}0&0&1\1&0&1\0&1&0\end{pmatrix}.
\]

Its characteristic polynomial is \(x^3-x-1\), so Newton sums or direct recurrence show \(R_n=\operatorname{tr}(M^n)\) for every \(n\ge0\). Exact integer multiplication gives

\[
M^{13}=\begin{pmatrix}7&9&12\12&16&21\9&12&16\end{pmatrix}
=I+3A,\qquad
A=\begin{pmatrix}2&3&4\4&5&7\3&4&5\end{pmatrix}.
\]

The initial residues are

\[
(R_0,R_1,\ldots,R_{12})=(3,0,2,3,2,5,5,7,10,12,17,22,29).
\]

Because \(M^{13}\equiv I\pmod3\), the only classes potentially divisible by \(3\) are \(r\in\{0,1,3,9\}\). This already proves the zero-valuation branch.

**2. The exceptional class \(r=0\).** As \(\operatorname{tr}(A)=12\), the binomial expansion of \((I+3A)^m\) yields

\[
R_{13m}=\operatorname{tr}((I+3A)^m)
\equiv 3+3m\operatorname{tr}(A)\equiv3\pmod9
\]

for every integer \(m\ge0\). In particular \(\nu_3(R_{13m})=1\).

**3. A sharp local isometry.** Fix \(r\in\{1,3,9\}\) and put

\[
F_r(m)=\frac{R_{13m+r}}3
=\frac{\operatorname{tr}(M^r(I+3A)^m)}3
\qquad(m\ge0).
\]

The division is integral by Step 1. Direct matrix products give

\[
(d_1,d_3,d_9)=
(\operatorname{tr}(M A),\operatorname{tr}(M^3 A),\operatorname{tr}(M^9 A))
=(17,29,158),
\]

so each \(d_r\) is a unit modulo \(3\). For every positive integer \(h\) and \(s=\nu_3(h)\), the binomial identity \(j\binom hj=h\binom{h-1}{j-1}\) implies

\[
\nu_3\!\left(3^j\binom hj\right)
\ge s+j-\nu_3(j)\ge s+2\quad(j\ge2).
\]

Consequently

\[
(I+3A)^h\equiv I+3hA\pmod{3^{s+2}}.
\]

Writing \(B=I+3A\), taking the trace of \(M^rB^m(B^h-I)\), and dividing by \(3\), we obtain

\[
F_r(m+h)-F_r(m)
\equiv h\operatorname{tr}(M^r A)
\pmod{3^{s+1}}.
\]

The right-hand side has valuation exactly \(s\). Interchanging two indices when necessary therefore proves

\[
\nu_3(F_r(m)-F_r(n))=\nu_3(m-n)
\quad(m\ne n;\ m,n\ge0).
\]

This identity shows that \(F_r\) extends uniquely to an isometry of \(\mathbb Z_3\) into itself. Each reduction \(F_r:\mathbb Z/3^j\mathbb Z\to\mathbb Z/3^j\mathbb Z\) is injective, hence bijective; the extension is therefore surjective. There is a unique \(\beta_r\in\mathbb Z_3\) with \(F_r(\beta_r)=0\). The isometry gives

\[
\nu_3(F_r(m))=\nu_3(m-\beta_r),
\]

proving the remaining valuation branch. Since \(F_1(0)=0\), \(\beta_1=0\). The two other roots are determined digit by digit by testing the three lifts of each solution to \(R_{13m+r}\equiv0\pmod{3^{j+1}}\). The verified eight-digit reductions are \(\beta_3\equiv4477\) and \(\beta_9\equiv2107\pmod{3^8}\). Positive terms satisfy \(R_n>0\) for \(n\ge2\) by the recurrence, so no other nonnegative integer index is a zero.

**4. Exact density and uniform discrepancy.** Each of the nine nonvanishing residue classes modulo \(13\) has density \(1/13\); hence \(p_0=9/13\). The class \(r=0\) contributes \(1/13\) to valuation one. In each of the three root classes, the condition \(\nu_3(m-\beta_r)=0\) selects two residues modulo \(3\), adding \(3\cdot2/(13\cdot3)=2/13\) and giving \(p_1=3/13\). For \(t\ge2\), each of the three root classes contributes two residue classes modulo \(3^t\), so \(p_t=3\cdot2/(13\cdot3^t)\).

At level zero the count is a union of nine arithmetic progressions modulo \(13\); at level one, one modulo \(13\) and six modulo \(39\); at every higher level, six modulo \(13\cdot3^t\). The number of members below \(N\) in any individual progression differs from its density times \(N\) by less than one. Removing the initial term \(n=0\), which belongs only to the valuation-one progression, changes that level by one; the exceptional zero \(n=1\) belongs to no finite valuation level. Summing the progression errors proves \(\lvert C_t(N)-p_tN\rvert\le9\) simultaneously for all \(t,N\). This completes the proof.

## Verification

The standalone file `VERIFY.py` contains only Python standard-library code. Execute `python3 VERIFY.py`. It checks the exact companion-matrix identity, all three unit slopes, unique root lifting through depth fifteen, 119,998 Perrin valuations computed independently by the recurrence modulo a large power of three, and the discrepancy inequality for 119,998 consecutive cutoffs at twelve valuation levels. The expected marker is `VERIFY_OK`. These checks are finite corroboration; the proof above supplies the unrestricted conclusion.

## Relationship to prior work

The classical normalization and sequence are documented in OEIS A001608 and Batte–Chalebgwa–Ddamulira (first public preprint May 16, 2021). The fully available 2021 Rihane–Togbé article cites existing *2-adic* valuation formulae for Perrin numbers (its Lemma 2.2) in a repdigit application; it does not treat ternary valuation levels or a uniform discrepancy law. Bravo–Irmak (2024) concerns 2-adic valuations of *shifted* Perrin numbers. These are neighboring methods and related arithmetic objects, not statements implying the present 3-adic root classification. The sequence table A001608 supplies values and references, not a classification of all ternary valuations. The distinctive conclusion here is the isometric root decomposition modulo thirteen and exact frequencies for all ternary valuation levels.

## Limitations

This theorem concerns one fixed recurrence and the prime three. It does not classify valuations at other odd primes, nor does it give a rational closed form for the two nontrivial 3-adic roots. The root-defining congruences are exact and effective. The literature search could miss an unindexed valuation theorem or an implicit special case of a broader local-linear-recurrence result. The proof and finite checks have not undergone independent validation.

## References

- Rihane, S. E., and Togbé, A., *Repdigits as products of consecutive Padovan or Perrin numbers*, Arabian Journal of Mathematics 10 (2021), 469–480, https://link.springer.com/article/10.1007/s40065-021-00317-1 (published March 28, 2021).
- Batte, H., Chalebgwa, T. P., and Ddamulira, M., *Perrin numbers that are concatenations of two distinct repdigits*, arXiv:2105.08515, https://arxiv.org/abs/2105.08515 (first public May 16, 2021).
- Bravo, E., and Irmak, N., *The 2-adic valuation of shifted Padovan and Perrin numbers and applications*, Turkish Journal of Mathematics 48 (2024), 1183–1196, https://journals.tubitak.gov.tr/math/vol48/iss6/13/.
- OEIS Foundation, *A001608: Perrin sequence*, https://oeis.org/A001608.
