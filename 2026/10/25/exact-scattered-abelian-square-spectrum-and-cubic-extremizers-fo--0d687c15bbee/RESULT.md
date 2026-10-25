# Exact scattered abelian-square spectrum and cubic extremizers for two-marked binary words

## Finding

For each nonnegative integer triple \(a,b,c\), let \(w=0^a1\,0^b1\,0^c\), \(s=a+b+c\), and \(n=s+2\). An **abelian square** is a nonempty even-length word whose first and second halves have identical symbol counts. A **scattered subsequence** is formed by deleting positions while preserving the order of retained positions. Let \(F(a,b,c)\) count **distinct abelian-square strings** that occur as scattered subsequences of \(w\), each counted once regardless of the number of embeddings.

Then the exact count is
\[
F(a,b,c)=\left\lfloor\frac{s}{2}\right\rfloor+
\sum_{i=0}^{a}\sum_{k=0}^{c}
\max\!\left\{0,1+\left\lfloor\frac{b-|i-k|}{2}\right\rfloor\right\}.
\tag{1}
\]
In particular, this also applies when one or more zero runs are empty.

For the exact length spectrum, put \(A_h=\min(a,h-1)\), \(C_h=\min(c,h-1)\), and define \(Q(t)=\max\{0,t(t-1)/2\}\) **only for integer \(t\ge2\)**, with \(Q(t)=0\) for integers \(t\le1\). Define
\[
H_{A,C}(t)=Q(t+2)-Q(t-A+1)-Q(t-C+1)+Q(t-A-C).
\]
For each integer \(1\le h\le\lfloor n/2\rfloor\), the number \(f_{2h}(a,b,c)\) of such distinct subsequences of length \(2h\) is
\[
f_{2h}(a,b,c)=\mathbf1_{\{2h\le s\}}+(A_h+1)(C_h+1)-H_{A_h,C_h}(2h-3-b).
\tag{2}
\]
There are no odd-length abelian squares, and all other lengths have zero count.

Let \(M(n)\) denote the maximum of \(F(a,b,c)\) over \(a,b,c\ge0\) with \(a+b+c=n-2\). Then, as \(n\to\infty\),
\[
\boxed{M(n)=\frac{2}{147}n^3+O(n^2).}
\tag{3}
\]
Moreover, a sequence of such triples with \(n\to\infty\) satisfies \(F(a,b,c)/n^3\to 2/147\) **if and only if**
\[
\left(\frac an,\frac bn,\frac cn\right)\longrightarrow
\left(\frac27,\frac37,\frac27\right).
\tag{4}
\]
The leading coefficient is attained by integer triples \((a,b,c)=(2m,3m,2m)\) with \(n=7m+2\). The two ones are the marked minority positions; exchanging symbols gives the same assertions.

## Assumptions and scope

All \(a,b,c\) are **nonnegative integers**; \(w\) always contains exactly two ones, even when their separating zero run is empty. The empty word is not an abelian square. Distinctness is **of subsequence strings**, not embeddings, not Parikh vectors, and not contiguous factors. Bounds involving \(n\) are for \(n\ge2\); the asymptotic statements concern integers \(n\to\infty\). The proof is entirely within binary combinatorics on words.

## Proof

**Step 1 (classification and exact total).** The distinct abelian-square subsequences containing no ones are exactly \(0^{2h}\) with \(1\le h\le\lfloor s/2\rfloor\). A nonempty abelian square cannot contain exactly one one; consequently, every other such subsequence contains both available ones and is uniquely of the form \(0^i1\,0^j1\,0^k\), with \(0\le i\le a\), \(0\le j\le b\), and \(0\le k\le c\). These run lengths uniquely determine the subsequence string, so there is no duplication between parameter triples.

A word \(0^i1\,0^j1\,0^k\) is an abelian square precisely when its length is even and its two ones lie in opposite halves. Setting its half-length to \(h=(i+j+k+2)/2\), those conditions are \(i,k\le h-1\), equivalent to \(j\ge |i-k|\), together with \(i+j+k\equiv0\pmod 2\). For each \((i,k)\), the possible middle lengths are exactly \(j=|i-k|,|i-k|+2,\ldots\) up to \(b\). Their number is the summand in (1). Adding the zero-only strings proves (1).

**Step 2 (length spectrum).** For total length \(2h\), the unique middle length is \(j=2h-2-i-k\). The two marked ones are in different halves iff \(0\le i\le A_h\) and \(0\le k\le C_h\). Nonnegativity of \(j\) follows automatically from these two inequalities, and the bound \(j\le b\) is equivalent to \(i+k\ge 2h-2-b\). Thus the two-one contribution counts integer lattice points in \([0,A_h]\times[0,C_h]\) above that diagonal. The number of points in this rectangle with \(i+k\le t\) is, by inclusion–exclusion on nonnegative integer pairs,
\[
\sum_{0\le i\le A}\sum_{0\le k\le C}\mathbf1_{\{i+k\le t\}}
=Q(t+2)-Q(t-A+1)-Q(t-C+1)+Q(t-A-C).
\]
Substitute \(t=2h-3-b\) to exclude points below the admissibility threshold, then add the optional zero-only word \(0^{2h}\), obtaining (2). Summing (2) gives (1) by classification.

**Step 3 (uniform continuous approximation).** Put
\[
V(a,b,c)=\int_0^a\int_0^c(b-|x-y|)_+\,dy\,dx,
\qquad t_+=\max(t,0).
\]
The number of admissible middle run lengths per \((i,k)\) differs from \((b-|i-k|)_+/2\) by at most one. The integrand is at most \(s\) and is Lipschitz in each coordinate with constant one. Comparing each unit lattice cell with the integrand at its corner and accounting for the boundary strips gives the **uniform** estimate
\[
F(a,b,c)=\frac12V(a,b,c)+O((s+1)^2),
\tag{5}
\]
where the absolute implied constant is independent of \(a,b,c\). This includes all boundary triples.

**Step 4 (unique continuous optimizer).** Fix a real total zero mass \(s>0\). For a fixed \(b>0\) and fixed \(a+c=s-b\), the integral \(V\) is uniquely largest at \(a=c=(s-b)/2\). Indeed, the layer-cake representation is
\[
V(a,b,c)=\int_0^b\operatorname{area}\{(x,y)\in[0,a]\times[0,c]:|x-y|\le r\}\,dr.
\]
For \(a>c\) and every \(r>0\), the derivative of this area with respect to \(c\), at fixed \(a\), is \(|[0,a]\cap[c-r,c+r]|\), and its derivative with respect to \(a\), at fixed \(c\), is \(|[0,c]\cap[a-r,a+r]|\). The former is **strictly larger** than the latter when \(a>c\) and \(r>0\): the shorter boundary segment lies at least as centrally within the longer interval, while the latter loses positive overlap at the farther boundary (including the cases \(r\ge a\)). Hence transferring any positive amount from the longer run to the shorter strictly raises the area and therefore \(V\). The case \(b=0\) has \(V=0\) and is not globally optimal.

Write \(\ell=(s-b)/2\). A change to diagonal-difference coordinates gives
\[
V(\ell,b,\ell)=2\int_0^{\min(b,\ell)}(\ell-u)(b-u)\,du
=\begin{cases}
\ell b^2-b^3/3,&0\le b\le\ell,\\
b\ell^2-\ell^3/3,&b\ge\ell.
\end{cases}
\tag{6}
\]
In the first regime \(b\le s/3\), the derivative is \(b(s-5b/2)>0\). In the second regime \(b\ge s/3\), substituting \(\ell=(s-b)/2\) gives derivative
\[
\frac{d}{db}V(\ell,b,\ell)=\frac{(s-b)(3s-7b)}8.
\]
It vanishes at the **unique** global maximum \(b=3s/7\), where \(a=c=2s/7\). The maximum equals \(4s^3/147\). Homogeneity of \(V\) and (5) prove the upper bound \(M(n)\le (2/147)n^3+O(n^2)\). Rounding the continuous maximizing triple, or taking \((2m,3m,2m)\), provides matching examples, proving (3).

**Step 5 (asymptotic rigidity).** The normalized continuous objective \(V(a,b,c)/s^3\) is continuous on the compact simplex \(a+b+c=s\), has the unique maximizing point \((2/7,3/7,2/7)\), and its discrete approximation error after dividing by \(n^3\) tends uniformly to zero. Therefore a sequence attains the limiting optimal coefficient precisely when its normalized triples converge to that point, proving (4).

## Verification

The bundled `verify.py` independently constructs all distinct subsequence strings by iterative extension for all \(7^3=343\) triples with \(0\le a,b,c\le6\), filters by equality of half-symbol counts, and compares each **length-specific count** with (2). It also checks the aggregate of (2) against a different difference-band enumeration for all \(17^3=4913\) triples with \(0\le a,b,c\le16\), including empty runs and adjacent ones. Scaled witnesses are checked as further diagnostics. Invoke `python3 verify.py` with standard Python; no third-party packages are needed. These finite tests are not used as proof of the universal theorem.

## Relationship to prior work

Richmond and Shallit (2008) enumerate abelian-square strings of specified length **over an entire alphabet**, without conditioning on their appearance as subsequences of a given source. Fici, Mignosi and Shallit (2017), Section 3, count distinct **contiguous abelian-square factors** and present the sparse-one construction \(0^m1\,0^m1\,0^m\), which produces quadratic factor growth. Their result supplies the motivation but neither determines the scattered-subsequence length spectrum nor the cubic extremum for the present fixed-source problem. Fici and Puzynina (2022) survey abelian-square factors, abelian repetitions and binomial/subsequence equivalence; their relevant sections were compared with the exact fixed-source statement. The present optimum balances the two outer zero runs in the ratio \(2:3:2\), unlike the optimization for contiguous factors.

## Limitations

The theorem is limited to binary words with **exactly two occurrences** of the minority symbol. It does not give the exact finite-length value of \(M(n)\) or all finite-length maximizing integer triples; it determines their sharp cubic leading asymptotics and rigidity. The empirical tests cover finite parameters only. The literature comparison supports originality relative to inspected sources, not an exhaustive certification against all unpublished or unindexed work. Independent verification of this research has not been performed.

## References

1. L. B. Richmond and J. Shallit, *Counting Abelian Squares*, 2008 preprint, arXiv:0807.5028; *Electronic Journal of Combinatorics* **16** (2009), R72. https://arxiv.org/abs/0807.5028
2. G. Fici, F. Mignosi and J. Shallit, *Abelian-Square-Rich Words*, first publicly posted 2017-01-04, arXiv:1701.00948, especially Section 3. https://arxiv.org/html/1701.00948v3
3. G. Fici and S. Puzynina, *Abelian Combinatorics on Words: a Survey*, first publicly posted 2022-07-20, arXiv:2207.09937, especially Sections 4.3 and 8.3. https://arxiv.org/html/2207.09937v2
