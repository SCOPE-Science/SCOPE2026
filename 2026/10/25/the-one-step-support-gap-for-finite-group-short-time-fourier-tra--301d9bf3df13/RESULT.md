# The one-step support gap for finite-group short-time Fourier transforms

## Finding

For every finite abelian group \(A\) of order \(N\ge3\) and all nonzero \(f,g\in\ell^2(A)\), the normalized short-time Fourier transform \(V_gf\) cannot have exactly \(N+1\) nonzero entries. Since \(|\operatorname{supp}V_gf|\ge N\), its support size is therefore either \(N\) or at least \(N+2\).

## Assumptions and scope

Write the finite abelian group additively, equip it with counting measure, and let \(\widehat A\) be its character group. The Fourier transform convention is
\[
\widehat h(\chi)=\sum_{y\in A}h(y)\overline{\chi(y)},\qquad \chi\in\widehat A.
\]
The normalized short-time Fourier transform is
\[
V_gf(x,\chi)=N^{-1/2}\sum_{y\in A}f(y)\overline{g(y-x)}\,\overline{\chi(y)}.
\]
No prime-order, positivity, or full-support hypothesis is imposed. The conclusion concerns cardinality only; it does not classify all attainable support sizes above the minimum.

## Proof

For each \(x\in A\), set
\[
h_x(y)=f(y)\overline{g(y-x)},\quad r_x=|\operatorname{supp}h_x|,\quad n_x=|\operatorname{supp}\widehat h_x|.
\]
Then \(V_gf(x,\cdot)=N^{-1/2}\widehat h_x\), so the total support size is \(M=\sum_{x\in A}n_x\). Put \(S=\operatorname{supp}f\), \(T=\operatorname{supp}g\), \(a=|S|\), and \(b=|T|\). The overlap counts satisfy
\[
r_x=|S\cap(T+x)|,\quad \sum_xr_x=ab,\quad J:=\{x:r_x>0\}=S-T.
\]
If \(k=|J|\), then \(k\ge\max(a,b)\), since for fixed \(t\in T\), the set \(S-t\) lies in \(S-T\), and for fixed \(s\in S\), the reflected translate \(s-T\) also lies in \(S-T\).

For any nonzero function \(h\) with \(r\) nonzero entries and \(n\) nonzero Fourier coefficients, Cauchy–Schwarz and Parseval give
\[
N\|h\|_2^2=\|\widehat h\|_2^2\le n\|\widehat h\|_\infty^2\le nr\|h\|_2^2.
\]
Thus \(rn\ge N\). Applying this to each nonzero \(h_x\), then using Cauchy–Schwarz on the positive numbers \(r_x\), yields
\[
M\ge N\sum_{x\in J}\frac1{r_x}\ge N\frac{k^2}{\sum_xr_x}=N\frac{k^2}{ab}.
\]
In particular \(M\ge N\).

We rule out \(M=N+1\) by cases.

**Case 1: \(a\ne b\).** Let \(m=\min(a,b)\). Since \(k\ge\max(a,b)\ge m+1\),
\[
M\ge N\frac{\max(a,b)^2}{ab}=N\frac{\max(a,b)}{m}\ge N\left(1+\frac1m\right)>N+1,
\]
because \(m\le N-1\). This contradicts \(M=N+1\).

**Case 2: \(a=b=m<N\).** If \(k\ge m+1\), then
\[
M\ge N\frac{(m+1)^2}{m^2}=N\left(1+\frac1m\right)^2>N+1,
\]
using \(N\ge m+1\). Otherwise \(k=m\). Every set \(S-t\), for \(t\in T\), has size \(m\) and lies in \(S-T\), also of size \(m\); hence all such sets equal \(S-T\). Therefore \(S\) is invariant under every difference of elements of \(T\). Its stabilizer \(H=\{u\in A:S+u=S\}\) contains \(T-T\), so \(T\) lies in one coset of \(H\). Since \(|T|=m\), \(|H|\ge m\); since \(S\) is a union of \(H\)-cosets and \(|S|=m\), \(|H|\) divides \(m\). Thus \(|H|=m\), and both \(S\) and \(T\) are cosets of \(H\).

Let \(H^\perp=\{\chi\in\widehat A:\chi(h)=1\text{ for every }h\in H\}\) and \(q=|H^\perp|=N/m\ge2\). For every \(x\in S-T\), the function \(h_x\) is supported on one full coset of \(H\). Its Fourier support is invariant under multiplication by \(H^\perp\): characters with the same restriction to \(H\) give Fourier coefficients equal up to a nonzero phase. Consequently each \(n_x\) is a multiple of \(q\), including the zero rows, so \(M\) is a multiple of \(q\). But \(N+1\equiv1\pmod q\), a contradiction.

**Case 3: \(a=b=N\).** All \(N\) rows \(h_x\) are nowhere zero, so every \(n_x\ge1\). If \(M=N+1\), exactly \(N-1\) rows have Fourier support one and the remaining row has support two. Let \(J_1=\{x:n_x=1\}\), so \(|J_1|=N-1\). For every \(d\in A\),
\[
|J_1\cap(J_1-d)|\ge N-2\ge1.
\]
Choose \(x,x+d\in J_1\). A function with Fourier support one is a scalar multiple of a character, hence \(h_{x+d}/h_x\) is a scalar character. On the other hand,
\[
\frac{h_{x+d}(y)}{h_x(y)}=\frac{\overline{g(y-x-d)}}{\overline{g(y-x)}}.
\]
As \(d\) was arbitrary, every ratio of two translates of \(g\) is a scalar character. Fix \(x_0\in J_1\). Since \(h_{x_0}\) is a scalar character and \(f,g\) are nowhere zero, the translate-ratio property forces every \(h_y\) to be a scalar character. Then every \(n_y=1\), giving \(M=N\), again a contradiction.

All cases contradict \(M=N+1\). Since \(M\) is an integer and \(M\ge N\), the only possibilities are \(M=N\) or \(M\ge N+2\).

## Verification

The row-wise inequality \(r_xn_x\ge N\) is proved directly from Parseval and Cauchy–Schwarz above, with the unnormalized finite-group Fourier transform specified in the assumptions. The three support-size cases exhaust \(1\le a,b\le N\). The subgroup case uses only the stabilizer of \(S\) and the annihilator cardinality \(|H^\perp|=N/|H|\); the full-support case uses the intersection bound \(|J_1\cap(J_1-d)|\ge N-2\), which is positive precisely for the stated range \(N\ge3\).

## Relationship to prior work

Nicola's 2022 preprint proves the minimum-support inequality and identifies equality cases on cyclic groups, with a necessary subgroup-coset conclusion for arbitrary finite abelian groups. The present statement addresses the next integer above that minimum, not the equality classification. Krahmer, Pfander, and Rashkov developed general support-size bounds for finite-abelian-group time-frequency representations, including bounds optimized over windows and prime-order refinements. A separately indexed result gives the stronger alternative \(N\) or at least \(2N\) for odd prime cyclic groups of order at least five; that restricted theorem does not cover all composite and noncyclic finite abelian groups. No claim is made that the present lower gap is sharp at \(N+2\).

## Limitations

The conclusion excludes exactly one support cardinality; it does not determine the smallest attainable support above \(N\), classify the \(N+2\) case, or extend to nonabelian groups. The condition \(N\ge3\) is necessary: on \(A=\mathbb Z_2\), with \(f=(1,1/2)\) and \(g=(1,2)\), the two row products are \(h_0=(1,1)\) and \(h_1=(2,1/2)\), whose Fourier supports have sizes one and two, so \(|\operatorname{supp}V_gf|=3=N+1\).

## References

1. F. Nicola, “The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality,” arXiv:2204.14176v1 (first public version 29 April 2022); *Journal of Functional Analysis* 284 (2023), article 109924. DOI: 10.1016/j.jfa.2023.109924.
2. F. Krahmer, G. E. Pfander, and P. Rashkov, “Uncertainty in time-frequency representations on finite Abelian groups and applications,” arXiv:math/0611493; *Applied and Computational Harmonic Analysis* 25 (2008), 209–225. DOI: 10.1016/j.acha.2007.09.008.
