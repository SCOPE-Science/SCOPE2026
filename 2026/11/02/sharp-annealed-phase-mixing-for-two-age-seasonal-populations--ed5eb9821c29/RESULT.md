# Sharp annealed phase mixing for two-age seasonal populations

## Finding
Consider the two-age Leslie projection matrices
\[
A=\begin{pmatrix}a&b\\c&0\end{pmatrix},\qquad
B=\begin{pmatrix}d&e\\f&0\end{pmatrix},
\]
with \(a,b,d,e>0\) and \(0<c,f\leq1\). Every year consists of three discrete demographic phases: two of type \(A\) and one of type \(B\). Two cyclic-phase arrangements have annual projection matrices \(X=A^2B\) and \(Y=ABA\). Both fixed arrangements have the same Perron growth factor. Suppose independently each year the first annual arrangement is used with probability \(p\in[0,1]\), and the other with probability \(1-p\). For a deterministic initial population vector \(z_0>0\), the annual mean population is governed by \(M_p=pX+(1-p)Y\).

Write
\[
t=a^2d+abf+ace+bcd,\quad \delta=-(bc)^2ef,\quad
J=bc\big[(bf-ce)^2+(ae-bd)(cd-af)\big].
\]
Then for every \(p\in[0,1]\) the expected-population asymptotic per-year growth factor is exactly
\[
\boxed{\rho(M_p)=\frac{t+\sqrt{t^2-4\delta+4Jp(1-p)}}2.}
\]
Consequently, when \(J>0\), independent random phase choices strictly increase the asymptotic growth factor of the expected population for every \(0<p<1\), and \(p=1/2\) is its unique maximizer. When \(J<0\), every nontrivial mixture strictly reduces that factor, with its unique minimum at \(p=1/2\). When \(J=0\), the factor is independent of \(p\). These alternatives exhaust all positive biologically admissible parameters.

There is an exact rational example with both deterministic phase arrangements below the unit growth threshold, but the randomized expected population above it. Choose
\[
A=\begin{pmatrix}1/2&1\\1/2&0\end{pmatrix},\qquad
B=\begin{pmatrix}1/2&3/2\\1/4&0\end{pmatrix}.
\]
For both fixed arrangements, the annual growth factor is \((7+\sqrt{73})/16<1\); for an independent annual mixture, **mean-population growth exceeds one if and only if** \(1/3<p<2/3\), with unique maximum \((7+\sqrt{82})/16>1\) at \(p=1/2\). Exactly at the two endpoints of that open interval the factor equals one.

## Assumptions and scope
The two age coordinates are a youngest and an older class. Fertility entries \(a,b,d,e\) may be any positive numbers; the progression/survival probabilities \(c,f\) lie in \((0,1]\). No older individual survives into the same older class, as encoded by the bottom-right zero. The model is a *linear expected-abundance projection*, not a finite-individual extinction process. Its year-to-year phase selections are independent, independent also of the current population, and identically distributed; the full three-phase inventory is unchanged in every year. The observed quantity is the long-term growth of \(\mathbb E[z_n]\), not the almost-sure growth of individual random realizations.

## Proof
Set \(X=A^2B\), \(Y=ABA\). Matrix-trace cyclicity gives \(\operatorname{tr}X=\operatorname{tr}Y=t\). Multiplicativity of the determinant gives \(\det X=\det Y=(\det A)^2\det B=\delta<0\). With \(E=X-Y\), the exact quadratic determinant expansion
\[
\det(Y+pE)=\det Y+p\bigl(\det X-\det Y-\det E\bigr)+p^2\det E
=\delta-p(1-p)\det E
\]
holds for any two-by-two matrices with equal determinant. Because \(X-Y=A(AB-BA)\), direct multiplication yields
\[
AB-BA=\begin{pmatrix}
bf-ce & ae-bd\\ cd-af&ce-bf
\end{pmatrix},
\]
and therefore \(\det E=J\) exactly as displayed. Hence \(\operatorname{tr}M_p=t\) and \(\det M_p=\delta-Jp(1-p)\).

Both \(X\) and \(Y\) have strictly positive entries. Thus every convex mixture \(M_p\) is a strictly positive two-by-two matrix, with strictly positive characteristic discriminant and a simple Perron eigenvalue equal to the larger root of its characteristic quadratic. This proves the displayed formula. The root is strictly increasing in \(Jp(1-p)\); the function \(p(1-p)\) is zero at the endpoints and has its unique maximum at \(p=1/2\). All three cases and equality statements follow. Since annual matrices are independent of earlier histories, \(\mathbb E[z_{n+1}]=M_p\mathbb E[z_n]\), and strictly positive Perron–Frobenius theory gives long-run mean-vector growth at rate \(\rho(M_p)\) for every positive initial vector.

In the rational example, direct multiplication gives
\[
X=\begin{pmatrix}1/2&9/8\\1/4&3/8\end{pmatrix},\qquad
Y=\begin{pmatrix}5/8&1/2\\1/2&1/4\end{pmatrix},
\]
so \(t=7/8\), \(\delta=-3/32\), and \(J=9/64\). The claimed endpoint and midpoint roots follow by substitution. For arbitrary \(p\), evaluating the characteristic polynomial at one gives
\[
\det(I-M_p)=1-t+\det M_p=\frac1{32}-\frac9{64}p(1-p).
\]
Here \(\det M_p<0\), so the second eigenvalue is negative and \(\rho(M_p)>1\) holds exactly when \(\det(I-M_p)<0\). This is equivalent to \(p(1-p)>2/9\), or \(1/3<p<2/3\). The strict inequalities \(\sqrt{73}<9<\sqrt{82}\) prove the threshold reversal without numerical approximation.

## Verification
The accompanying standalone Python 3 program `artifacts/verify.py` uses only exact rational arithmetic and the standard library. Execute `python3 artifacts/verify.py`. It checks 16,128 exact mixture-determinant identities over a finite parameter grid, as well as the complete rational witness, the eigenvalue discriminants, and the exact \((1/3,2/3)\) threshold. The general infinite-parameter claim follows from the analytical proof, not from finite testing.

## Relationship to prior work
Caswell and Trevisan (1994) established the sensitivity framework for fixed periodic matrix population products. Mertens et al. (2006) explicitly explained the equal asymptotic growth of cyclically permuted deterministic environments and studied their differing transient responses; their complete article does not formulate independent *annual random switching between cyclic phase choices* or this exact two-age growth trichotomy. Benaïm and Schreiber (2009) developed a theory of persistence based on the *almost-sure Lyapunov exponent* in random environments; its biological persistence criterion is distinct from the expected-population Perron factor analyzed here. Cáceres and Cáceres-Saez (2010) studied random Leslie vital-rate variation and showed that randomness can alter *effective expected-population growth*, including threshold behavior. That general random-growth phenomenon is prior art: only the sharp commutator criterion and the exact phase-mixture reversal for two cyclically equivalent annual arrangements are assessed here. Caswell and Shyu (2012) developed a general sensitivity analysis for periodic matrix models; an abstract-level comparison did not resolve every possible implication of that paper.

## Limitations
Growth of an *expected* population does not demonstrate positive almost-sure growth, finite-population survival or persistence in a density-regulated biological model. Rare high-growth realizations may dominate expectations. The result assumes independence of annual phase choice and strict two-age Leslie form; it says nothing about random phase choices correlated between years, arbitrary structured matrices or stochastic per-capita growth rates. The originality comparison is provisional: general matrix-pencil theory or related ecological random-product work could subsume the exact specialization. The closed criterion and rational interval remain self-contained mathematical statements irrespective of historical priority.

## References
- Caswell, H. and Trevisan, M. C. (1994), “Sensitivity Analysis of Periodic Matrix Models,” *Ecology* 75, 1299–1303, DOI: 10.2307/1937455; first published 1994-07-01.
- Mertens, S. K., Yearsley, J. M., van den Bosch, F. and Gilligan, C. A. (2006), “Transient population dynamics in periodic matrix models: methodology and effects of cyclic permutations,” *Ecology* 87, 2338–2348, DOI: 10.1890/0012-9658(2006)87[2338:TPDIPM]2.0.CO;2; first published 2006-09-01.
- Benaïm, M. and Schreiber, S. J. (2009), “Persistence of structured populations in random environments,” *Theoretical Population Biology* 76, 19–34, DOI: 10.1016/j.tpb.2009.03.007; online 2009-04-07.
- Cáceres, M. O. and Cáceres-Saez, I. (2010), “Random Leslie matrices in population dynamics,” *Journal of Mathematical Biology* 63, 519–556, DOI: 10.1007/s00285-010-0378-0; published online 2010-11-14.
- Caswell, H. and Shyu, E. (2012), “Sensitivity analysis of periodic matrix population models,” *Theoretical Population Biology* 82, 329–339, DOI: 10.1016/j.tpb.2012.03.008; published 2012-04-30.
