# Sharp \(n^{-1}\) total-variation dependence of fixed and cyclic points in uniform random mappings

## Finding
Let \(n\ge1\) be an integer and let \(f:[n]\to[n]\) be a map chosen uniformly from the \(n^n\) maps. Write \(F_n=\#\{i:f(i)=i\}\) for its number of fixed points and \(K_n=\#\{i:i\text{ lies on a directed cycle of }f\}\) for its number of cyclic points. Define the **dependence distance**
\[
 d_n=d_{\mathrm{TV}}\bigl(\mathcal L(F_n,K_n),\mathcal L(F_n)\otimes\mathcal L(K_n)\bigr),
\]
where total variation of two probability masses is half their \(\ell^1\) distance. Then
\[
 \boxed{\operatorname{Cov}(F_n,K_n)=0\quad\text{for every }n\ge1}
\]
and
\[
 \boxed{\lim_{n\to\infty}n d_n=\frac{3e^2+1}{8}+\frac{3}{4e}
       =3.1718056179775755\ldots.}
\]
For every \(n\ge2\), the variables are nevertheless dependent, so \(d_n>0\). This is an exact first-order asymptotic for their dependence, not merely a bound.

An exact finite-size formula is as follows. Define \((n)_k=n(n-1)\cdots(n-k+1)\),
\[
 q_{n,k}=\frac{k(n)_k}{n^{k+1}}\quad(1\le k\le n),\qquad
 b_{n,j}=\binom nj\frac{(n-1)^{n-j}}{n^n}\quad(0\le j\le n),
\]
and the rencontres distribution
\[
 r_{k,j}=\frac1{j!}\sum_{\ell=0}^{k-j}\frac{(-1)^\ell}{\ell!}
 \quad(0\le j\le k),\qquad r_{k,j}=0\quad(j>k).
\]
Then
\[
 \boxed{d_n=\frac12\sum_{k=1}^{n}q_{n,k}\sum_{j=0}^{n}|r_{k,j}-b_{n,j}|.}
\]
In particular, \(d_2=1/2\), \(d_3=109/243\), and \(d_4=3235/8192\).

## Assumptions and scope
The images \(f(1),\ldots,f(n)\) are independent and uniform on \([n]\). A directed cycle of length one is a fixed point; a cyclic point is a vertex on a cycle of any length. A point feeding into a cycle but not on it is not cyclic. The claim concerns the **unconditioned uniform mapping** model; it does not assert the same constant for mappings with a prescribed indegree profile, for conditioned connected mappings, or for random permutations. All displayed finite-size identities include \(n=1\), with \(d_1=0\).

## Proof
**1. Exact decomposition.** Fix \(1\le k\le n\). To form a map with exactly \(k\) cyclic vertices, choose the cyclic set, place a permutation on that set, and attach the remaining vertices as a directed forest rooted at the cyclic set. The number of such forests with a specified \(k\)-element root set is \(k n^{n-k-1}\); this follows, for example, from the complete-graph rooted-forest matrix-tree formula, and yields one forest for \(k=n\). Thus
\[
 \Pr(K_n=k)=\frac{\binom nk k!\, k n^{n-k-1}}{n^n}=q_{n,k}.
\]
All permutations on the cyclic set have equally many rooted-forest extensions. Consequently, conditional on \(K_n=k\), the number \(F_n\) is the number of fixed points in a uniform permutation of \(k\) objects. Inclusion-exclusion gives \(r_{k,j}\). Unconditionally the events \(f(i)=i\) are independent Bernoulli events with probability \(1/n\), so \(F_n\sim\operatorname{Bin}(n,1/n)\) and its mass is \(b_{n,j}\). The displayed finite-size formula for \(d_n\) follows by disintegrating total variation over the common \(K_n\)-marginal.

**2. Zero covariance despite dependence.** Every uniform permutation on a nonempty finite set has expected fixed-point count one; hence \(\mathbb E[F_n\mid K_n]=1\) and \(\operatorname{Cov}(F_n,K_n)=0\). For \(n\ge2\), \(K_n=1\) forces \(F_n=1\), whereas the unconditioned binomial law assigns positive mass to \(F_n=0\). Independence therefore fails.

**3. Isolate the Poisson contribution.** Put \(P=\operatorname{Poisson}(1)\), \(R_k=\mathcal L(\text{fixed points of a uniform permutation on }k\text{ symbols})\), \(B_n=\operatorname{Bin}(n,1/n)\), \(\delta_k=d_{\mathrm{TV}}(R_k,P)\), and \(\Delta_n=d_{\mathrm{TV}}(B_n,P)\). By the triangle inequality,
\[
 \bigl|d_{\mathrm{TV}}(R_k,B_n)-\Delta_n\bigr|\le\delta_k.
\]
Also \(nq_{n,k}=k\prod_{a=0}^{k-1}(1-a/n)\le k\), with \(nq_{n,k}\to k\) for each fixed \(k\). In Step 4 we show \(\sum_{k\ge1}k\delta_k<\infty\). Since \(B_n\to P\) in total variation, dominated convergence applied to the exact decomposition gives
\[
 \lim_{n\to\infty}n(d_n-\Delta_n)=\sum_{k=1}^{\infty}k\delta_k.
\]
This argument controls the entire range of cyclic counts, including the typical \(\sqrt n\)-scale, rather than truncating it heuristically.

**4. Evaluate the weighted rencontres error.** Write \(s_m=\sum_{\ell=0}^m(-1)^\ell/\ell!\). The alternating-series remainder \(s_m-e^{-1}\) is positive for even \(m\) and negative for odd \(m\). Thus, because probabilities sum to one,
\[
 \delta_k=\sum_{\substack{0\le m\le k\\m\text{ even}}}
       \frac{s_m-e^{-1}}{(k-m)!}.
\]
For even \(m\), Taylor's integral remainder supplies the nonnegative representation
\[
 s_m-e^{-1}=\frac1{m!}\int_0^1e^{-t}(1-t)^m\,dt.
\]
Tonelli's theorem and \(\sum_{j\ge0}(j+m)/j!=(m+1)e\) (the omitted \(m=j=0\) term is zero) give
\[
 \sum_{k\ge1}k\delta_k
 =e\sum_{\substack{m\ge0\\m\text{ even}}}(m+1)(s_m-e^{-1})
 =\int_0^1e^u(\cosh u+u\sinh u)\,du
 =\frac{3e^2+1}{8}.
\]
In particular this establishes the required summability without a numerical tail assumption.

**5. The binomial-to-Poisson contribution.** For each fixed nonnegative \(j\), elementary expansion of the binomial mass yields
\[
 n\left(b_{n,j}-\frac{e^{-1}}{j!}\right)
 \longrightarrow\frac{e^{-1}}{j!}\frac{-j^2+3j-1}{2}.
\]
The convergence may be summed in absolute value: for \(j\le\lceil3\log n\rceil\), expand the logarithm of \(e b_{n,j}j!\) with a remainder bounded by \(O((1+j^4)/n^2)\) after multiplying by \(e^{-1}/j!\); above this cutoff, both factorial tails multiplied by \(n\) vanish. The limiting signed coefficients are positive only at \(j=1,2\), and their sum is \(3/(4e)\). It follows that
\[
 \lim_{n\to\infty}n\Delta_n=\frac12\sum_{j\ge0}\frac{e^{-1}}{j!}\left|\frac{-j^2+3j-1}{2}\right|=\frac3{4e}.
\]
Combining Steps 3–5 proves the sharp constant.

## Verification
The standalone `verify.py` performs exact rational comparisons against direct enumeration of all mappings for sizes \(1\le n\le6\), confirms the conditional rencontres law, the binomial and cyclic-count marginals, the exact total-variation formula, and covariance cancellation. It reported 231 exact/finite checks passed. The program separately compares a finite rencontres-error sum with the analytically derived limiting constant (one numerical consistency check). All asymptotic and infinite-sum claims follow from the proof above; finite checks are not offered as infinite certificates.

## Relationship to prior work
The conditional uniform-permutation decomposition for cyclic points is classical and explicitly discussed by Finch (2022, Section 3) and Hansen–Jaworski (2010, Section 1). It implies the finite joint distribution above after including the classical rencontres formula, so **the finite joint formula, conditional mean, and zero covariance are not asserted to be historically new independently**. Booher and collaborators (arXiv:2205.00135, Section 3.3) develop fixed-point-marked generating functions for a random map, also providing broad prior enumeration. The claim assessed as the contribution here is specifically the sharp \(n^{-1}\) total-variation dependence asymptotic with its explicit closed constant, which was not identified in the inspected statements. Generic Poisson convergence and asymptotic independence do not determine this first-order constant.

## Limitations
This result concerns only uniform random endofunctions and the scalar pair \((F_n,K_n)\); it does not give first-order approximations for the full cycle-length vector, nor a second-order error expansion for \(d_n\). Equivalent older derivations in mapping enumerations or conditioned-permutation approximation literature remain a historical-priority risk. The independent historical-priority question remains open.

## References
1. S. Finch, *Components and Cycles of Random Mappings*, arXiv:2205.05579v1 (first public 2022-05-11), especially Section 3. https://arxiv.org/abs/2205.05579
2. J. C. Hansen and J. Jaworski, *Random Mappings with a Given Number of Cyclical Points*, Ars Combinatoria 94 (2010), 341–359, especially Sections 1–2. https://combinatorialpress.com/ars-articles/volume-094-ars-articles/random-mappings-with-a-given-number-of-cyclical-points/
3. J. Booher et al., *Failing to Hash Into Supersingular Isogeny Graphs*, arXiv:2205.00135, especially Section 3.3 on random functions with fixed points. https://arxiv.org/abs/2205.00135
4. P. Flajolet and A. M. Odlyzko, *Random Mapping Statistics*, Advances in Cryptology—EUROCRYPT 1989, Lecture Notes in Computer Science 434 (1990), 329–354. https://doi.org/10.1007/3-540-46885-4_34
