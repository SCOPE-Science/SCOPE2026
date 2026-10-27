# Parity-dependent polynomial prefactors for Katetov types over capped geodesics

## Finding
Fix an integer \(D\ge 2\). Let \(A_{D,n}=\{p_1,\ldots,p_n\}\) be the individually named \(n\)-point metric space with \(d(p_i,p_j)=\min\{|i-j|,D\}\), and let \(T_D(n)\) count nonalgebraic complete one-point types over these parameters in the countable homogeneous universal metric space with distances \(\{0,1,\ldots,D\}\). The asymptotic is taken as \(n\to\infty\) with \(D\) fixed.

Put \(m=\lfloor D/2\rfloor+1\), \(\lambda_D=1+2\cos(\pi/(m+1))\), and \(v_j=\sin(j\pi/(m+1))\) for \(1\le j\le m\). Write \(S=\sum_{j=1}^m v_j\) and \(Q=\sum_{j=1}^m v_j^2\).

For **even** \(D\), the exact leading asymptotic is
\[
T_D(n)\sim C_D\lambda_D^n,\qquad C_D=\frac{S^2}{\lambda_D Q}>0.
\]
For **odd** \(D=2r+1\), form the \((r+2)\)-by-\((r+2)\) matrix \(B\), indexed by \(r,r+1,\ldots,D\), with \(B_{ij}=1\) when \(|i-j|\le1\) and zero otherwise; let \(q_L=(B^{L-1})_{r,r}\), for \(1\le L\le D\). Then
\[
T_D(n)\sim c_D n\lambda_D^n,\qquad
c_D=\frac{S^2v_1^2}{Q^2}\sum_{L=1}^{D}\frac{q_L}{\lambda_D^{L+2}}>0.
\]
Indeed, in the odd case \(T_D(n)=c_D n\lambda_D^n+O_D(\lambda_D^n)\). Thus **consecutive even and odd distance bounds have the same exponential growth rate but differ by an asymptotically linear factor**:
\[
\frac{T_{2r+1}(n)}{T_{2r}(n)}\sim\frac{c_{2r+1}}{C_{2r}}n\quad (r\ge1).
\]
The dominant coefficients are explicit finite expressions for every fixed diameter. For example, \(C_4=(1+\sqrt2)/2\), whereas \(c_5\approx0.1194263558534\). At diameter three, the entire generating function specializes to \(T_3(n)=(4n+21)2^{n-4}\) for \(n\ge4\), with \(T_3(1)=3\), \(T_3(2)=7\), and \(T_3(3)=17\). This diameter-three specialization is included for verification and is not asserted to be independent of previously known general diameter-three type-count identities.

## Assumptions and scope
The base \(A_{D,n}\) is a truncated unit-edge path metric; the parameters are individually named and pairwise distinct. The ambient structure realizes every admissible finite extension with distances in \(\{1,\ldots,D\}\). One-point types considered here require the new point to be distinct from every parameter. Algebraic equality types are excluded; adding them would increase the count by exactly \(n\) and would not change the asymptotics. The conclusions are pointwise in fixed \(D\), not uniform as \(D\) grows with \(n\).

For proof, let \(A\) denote the \(m\)-by-\(m\) tridiagonal matrix with ones on the main and immediately neighboring diagonals, indexed by the high labels \(\lceil D/2\rceil,\ldots,D\). Its Perron eigenvalue is \(\lambda_D\), with strictly positive eigenvector \((v_1,\ldots,v_m)\).

## Proof
**1. Types as constrained words.** By homogeneous finite-metric one-point extension, a nonalgebraic type is specified uniquely by positive distances \(f_i=d(x,p_i)\in\{1,\ldots,D\}\) such that \(|f_i-f_j|\le\min\{|i-j|,D\}\le f_i+f_j\) for every pair. The left inequalities are equivalent to the nearest-neighbor requirements \(|f_{i+1}-f_i|\le1\): necessity is immediate; for sufficiency telescope the adjacent differences and note that all labels lie in \([1,D]\), so \(|f_i-f_j|<D\).

**2. High labels and the transfer matrix.** Let \(h=\lceil D/2\rceil\). If every label lies in \([h,D]\), all lower triangle inequalities hold because \(2h\ge D\). Hence these admissible words are exactly the nearest-neighbor walks of length \(n-1\) on the looped path matrix \(A\), numbering \(H_n=\mathbf 1^{\mathsf T}A^{n-1}\mathbf 1\). The spectral decomposition of the symmetric path matrix gives
\[
H_n=\frac{S^2}{Q}\lambda_D^{n-1}+O_D(\nu_D^n)
\]
for some \(0\le\nu_D<\lambda_D\), because every other eigenvalue has strictly smaller absolute value. The displayed sine vector diagonalizes \(A\) and gives its Perron coefficient.

**3. Very low distances are exponentially negligible.** Choose an index with \(f_i=s\le\lfloor D/2\rfloor-1\), if one exists. Every index at separation at least \(D\) must have \(f_j\ge D-s\ge\lfloor D/2\rfloor+2\) when \(D\) is odd, or \(f_j\ge D/2+1\) when \(D\) is even. The bounded window of at most \(2D-1\) positions surrounding \(i\) has at most \(D^{2D-1}\) assignments. Beyond it, both tails have labels in a consecutive alphabet of at most \(\lfloor D/2\rfloor\) elements and adjacent changes at most one. Their total weight is bounded by a constant times \(\mu_D^n\), where
\[
\mu_D=1+2\cos\!\left(\frac{\pi}{\lfloor D/2\rfloor+1}\right)<\lambda_D
\]
when \(\lfloor D/2\rfloor\ge2\). Summing over the possible index \(i\) gives \(O_D(n\mu_D^n)\). For \(D\in\{2,3\}\), the relevant very-low set is empty. This estimate is an upper bound, so the local assignments need not themselves all be admissible.

**4. Even diameter.** When \(D=2r\), every distance outside the high alphabet \(\{r,\ldots,2r\}\) is very low in the sense of step 3. Thus \(T_D(n)=H_n+O_D(n\mu_D^n)\), proving the even case and its positive coefficient.

**5. Odd diameter and localized critical defects.** For \(D=2r+1\), after removing step-3 negligible words, labels belong to \(\{r,\ldots,D\}\). Every pair involving at least one label \(\ge r+1\) satisfies the lower triangle inequality, while two entries both equal to \(r\) satisfy it precisely when their separation is at most \(D-1\). Thus all occurrences of \(r\) lie in one contiguous span from the first to the last such occurrence, of length \(L\le D\). A span of length \(L\), including both endpoints labelled \(r\), has exactly \(q_L=(B^{L-1})_{r,r}\) admissible internal words. The prefixes and suffixes use only the high labels.

Let \(a_0=1\), and for \(k\ge1\) put \(a_k=e_1^{\mathsf T}A^{k-1}\mathbf 1\), where \(e_1\) indicates the smallest high label \(r+1\). Because the entries immediately adjacent to an occurrence of \(r\), when present, must equal \(r+1\), this gives the **exact finite convolution**
\[
\#\{\text{admissible words with all labels }\ge r\}
=H_n+\sum_{L=1}^{\min(D,n)}q_L\sum_{k=0}^{n-L}a_ka_{n-L-k}.
\]
By symmetry and Perron decomposition,
\[
a_k=\frac{Sv_1}{Q}\lambda_D^{k-1}+O_D(\nu_D^k)\qquad(k\ge1).
\]
Consequently the inner convolution equals
\[
\frac{S^2v_1^2}{Q^2}\,n\lambda_D^{n-L-2}+O_D(\lambda_D^{n-L-1})
\]
for every fixed \(1\le L\le D\). Summing the finite set of spans and adding the exponentially negligible smaller labels proves the odd coefficient \(c_D\) and its \(O_D(\lambda_D^n)\) remainder.

**6. Paired-diameter ratio.** Both \(D=2r\) and \(D=2r+1\) have \(m=r+1\) and hence the same positive Perron rate \(\lambda_D\). Dividing their leading asymptotics proves the linear ratio. The finite formulas for \(D=3\) follow from the convolution with \(q_1,q_2,q_3=(1,1,2)\), \(a_0=1\), and \(a_k=2^{k-1}\) for \(k\ge1\).

## Verification
A standalone standard-library Python checker separately enumerates all distance vectors and computes an exact finite-memory transfer recurrence. They agree for \(2\le D\le7\) and \(1\le n\le6\) (36 configurations). For odd \(D\in\{3,5,7\}\), the finite-memory recurrence restricted to labels \(\ge\lfloor D/2\rfloor\) agrees with the explicit defect-span convolution through \(n=14\). The exact diameter-three formula is checked through \(n=24\). The checker also reports the predicted positive Perron constants for diameters two through seven. These computations check small instances only; the all-diameter asymptotics rest on the proof above.

Run \(`python3 verification.py`\) with the Python 3 standard library.

## Relationship to prior work
Sauer's treatment of finite-distance Urysohn spaces identifies admissible Katětov type-functions and the one-point extension principle. Mbombo and Pestov likewise present the general extension correspondence. These facts underwrite the passage from metric types to distance words; neither source provides the capped-geodesic parity-prefactor asymptotics stated here.

Mubayi and Terry establish a distinct global even/odd structural contrast in the enumeration of **all** labelled finite integer-valued metric spaces. Their results do not determine one-point type counts above a fixed capped-geodesic parameter space. The published Widom–Rowlinson interpretation of the diameter-three one-type polynomial implies related special-case counts at \(D=3\); the diameter-three example above is not claimed as independent novelty. The main assertion concerns the all-diameter spectral law, explicit leading constants, and linear separation between consecutive bounds.

## Limitations
The asymptotics keep the distance bound fixed as the path grows, and do not claim uniformity for varying bounds, cyclic parameter metrics, or arbitrary base graphs. The exact convolution isolates the dominant odd-diameter label range but is not an exact full-type formula for every odd \(D\ge5\), because rarer smaller-distance labels are bounded rather than enumerated in that identity. A related published diameter-three type-polynomial result was examined in full; it does not state the all-diameter spectral asymptotic. Unindexed or implicit generalizations remain an originality risk.

## References
1. N. W. Sauer, *Vertex partitions of metric spaces with finite distance sets*, arXiv:1010.4212 (first posted 2010-10-20), especially Section 2 on Katětov type functions and homogeneous finite-distance spaces. https://arxiv.org/abs/1010.4212
2. B. Mbombo and V. G. Pestov, *Subgroups of isometries of Urysohn–Katětov metric spaces of uncountable density*, arXiv:1012.1056 (2010), especially Section 2. https://arxiv.org/abs/1012.1056
3. D. Mubayi and C. Terry, *Discrete metric spaces: structure, enumeration, and 0–1 laws*, arXiv:1502.01212 (first posted 2015-02-04), especially Sections 1.1–1.2. https://arxiv.org/abs/1502.01212
4. *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space*, published mathematical record (full result text examined), 2026.
