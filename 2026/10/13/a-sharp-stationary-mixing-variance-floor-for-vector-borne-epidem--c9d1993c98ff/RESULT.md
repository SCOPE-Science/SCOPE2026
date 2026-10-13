# A sharp stationary-mixing variance floor for vector-borne epidemic reproduction

## Finding

In the homogeneous-parameter hybrid Lagrangian–Eulerian Ross–Macdonald model of Gao and Yuan [1], fix the host-group population proportions, the host residence matrix, the vector stationary patch proportions and the common epidemiological parameters, but allow the **vector migration generator** to vary over every irreducible conservative generator with that same stationary vector. Then the exact infimum of the squared reproduction-number ratio is the weighted second moment of the host groups' relative vector exposure. Specifically, with the definitions below,

\[
\inf_{D\in\mathcal G(v)}\frac{\mathcal R_0(D)^2}{\mathcal R_{\mathrm{hom}}^2}
=\sum_{k=1}^{m}h_kq_k^2
=1+\sum_{k=1}^{m}h_k(q_k-1)^2=:M.
\]

For **every** admissible finite generator, the ratio is at least \(M\). When the exposures \(q_k\) are not all equal, the inequality is **strict** for every such generator, but the bound is approached by an explicit arbitrarily fast, irreducible mixing family. When the exposures are all equal, they necessarily all equal one, and \(\mathcal R_0(D)=\mathcal R_{\mathrm{hom}}\) for **every** admissible generator. Consequently, this gives the necessary and sufficient equality criterion for the homogeneous single-patch lower bound asked for in the discussion of [1], even if patchwise vector and effective-host proportions are unequal.

## Assumptions and scope

Let \(m,n\geq1\) be integers. Let the fractions \(h_k>0\) sum to one, and let the host residence matrix \(P=(p_{ki})\in[0,1]^{m\times n}\) have each row sum one. Every vector patch is used by hosts: \(s_i:=\sum_{k=1}^{m}h_kp_{ki}>0\) for \(1\leq i\leq n\). Fix a vector stationary distribution \(v_i>0\), \(\sum_i v_i=1\), and write

\[
 r_i=\frac{v_i}{s_i},\qquad q_k=\sum_{i=1}^{n}p_{ki}r_i,\qquad
 M=\sum_{k=1}^{m}h_k q_k^2.
\]

Every \(q_k\) is positive, and \(\sum_kh_kq_k=1\); hence \(M=1+\operatorname{Var}_{h}(q)\). Fix \(a,b,c,\gamma,\mu,H,V>0\), and take identical biting, transmission, recovery and vector death parameters in all groups and patches, as in Corollary 4.4 of [1]. The single-patch reference reproduction number is

\[
 \mathcal R_{\mathrm{hom}}=\sqrt{\frac{a^2bcV}{\mu\gamma H}}.
\]

For \(n\geq2\), let \(\mathcal G(v)\) be the collection of finite real \(n\times n\) irreducible Metzler matrices \(D\) satisfying \(\mathbf 1^{\mathsf T}D=0\) and \(Dv=0\). Thus the off-diagonal entries are nonnegative travel rates, columns sum to zero, and \(v\) is the stationary vector. For \(n=1\), take \(\mathcal G(v)=\{0\}\). We impose no reversibility, symmetry, upper-rate cutoff or requirement that the rows of \(P\) be distinct. All quantities and limits refer to fixed \(h,P,v,a,b,c,\gamma,\mu,H,V\).

The next-generation reduction from [1, equations (4.2)–(4.4), Corollary 4.4] is

\[
 L=\operatorname{diag}(v_i/s_i)\,P^{\mathsf T}\operatorname{diag}(h_k)P\operatorname{diag}(1/s_i),
 \qquad K_D=(\mu I-D)^{-1}L,
\]
\[
 \frac{\mathcal R_0(D)^2}{\mathcal R_{\mathrm{hom}}^2}=\mu\rho(K_D).
\]

Here \(\rho\) denotes spectral radius. The theorem addresses the basic reproduction number of this homogeneous-parameter, positive-host-share model; it does not assert the corresponding claims for heterogeneous rates, host-free patches, finite maximal travel rates, or disease prevalence.

## Proof

**1. Well-posed Perron reduction.** For \(n\geq2\), the matrix \(\mu I-D\) is an invertible nonsingular \(M\)-matrix and its inverse is strictly positive: \((\mu I-D)^{-1}=\int_0^{\infty}e^{-\mu t}e^{tD}\,dt\), with all entries of \(e^{tD}\) positive for \(t>0\) by irreducibility. Each column of \(L\) has a positive entry because \(s_j>0\), and hence \(K_D\) is strictly positive. Choose a Perron eigenvector \(y\gg0\) and eigenvalue \(\lambda=\rho(K_D)>0\), so

\[
 Ly=\lambda(\mu I-D)y.
\]

Write \(z_i=y_i/v_i>0\). The balanced nonnegative flows \(F_{ij}=d_{ij}v_j\) for distinct \(i,j\) obey \(\sum_{j\ne i}F_{ij}=\sum_{j\ne i}F_{ji}\), because \(Dv=0\) and \(\mathbf 1^{\mathsf T}D=0\). Dividing the last eigen-equation coordinatewise by \(z_i\) and summing yields

\[
 \sum_i\frac{(Ly)_i}{z_i}=\lambda\left(\mu-\sum_i\frac{(Dy)_i}{z_i}\right).
\]

The migration term is nonnegative, by the elementary entropy inequality \(u-1\geq\log u\):

\[
 \begin{aligned}
 E:=\sum_i\frac{(Dy)_i}{z_i}
 &=\sum_{i\ne j}F_{ij}\left(\frac{z_j}{z_i}-1\right)\\
 &\geq\sum_{i\ne j}F_{ij}(\log z_j-\log z_i)=0.
 \end{aligned}
\]

The last equality is flow balance. Equality \(E=0\) forces \(z_i=z_j\) on every directed edge with positive flow. Irreducibility implies \(z\) is constant, equivalently \(y\) is proportional to \(v\).

**2. Groupwise Cauchy–Schwarz bound.** Expanding the matrix \(L\) and interchanging finite sums gives

\[
 \begin{aligned}
 \sum_i\frac{(Ly)_i}{z_i}
 &=\sum_k h_k
   \left(\sum_i\frac{p_{ki}v_i^2}{s_i y_i}\right)
   \left(\sum_j\frac{p_{kj}y_j}{s_j}\right)\\
 &\geq\sum_k h_k\left(\sum_i\frac{p_{ki}v_i}{s_i}\right)^2
 =\sum_kh_kq_k^2=M.
 \end{aligned}
\]

The inequality is Cauchy–Schwarz applied separately to each group \(k\), including when some \(p_{ki}=0\). Combining with Step 1 yields \(M\leq\lambda(\mu-E)\leq\lambda\mu\).

**3. Rigidity of equality and full baseline equality classification.** If \(\lambda\mu=M\), both inequalities in Step 2 must be equalities, and \(E=0\), so \(y=cv\) for some \(c>0\). Since \(Dv=0\), the eigen-equation implies \(Lv=Mv\). Let \(q=Pr\) and \(s=P^{\mathsf T}h\), where vector products use the dimensions defined above. The coordinate identity for \(Lv=Mv\) is

\[
 P^{\mathsf T}\operatorname{diag}(h)(q-M\mathbf 1_m)=0.
\]

Because \(q-M\mathbf 1_m=P(r-M\mathbf 1_n)\), take its inner product against \(r-M\mathbf 1_n\) to deduce

\[
 \sum_kh_k(q_k-M)^2=0.
\]

Thus every \(q_k=M\). The identity \(\sum_kh_kq_k=1\) yields \(M=1\) and \(q_k=1\) for every group. Conversely, if all \(q_k=1\), put \(B=\operatorname{diag}(v/s)P^{\mathsf T}\), \(A=P\operatorname{diag}(h)\operatorname{diag}(1/s)\). Then \(L=BA\), \(\mathbf 1_n^{\mathsf T}B=\mathbf 1_m^{\mathsf T}\), \(\mathbf 1_m^{\mathsf T}A=\mathbf 1_n^{\mathsf T}\), and \(\mathbf 1_n^{\mathsf T}(\mu I-D)^{-1}=\mu^{-1}\mathbf 1_n^{\mathsf T}\). Hence all columns of \(K_D\) sum to \(1/\mu\), forcing \(\lambda=1/\mu\). We have proved

\[
 \frac{\mathcal R_0(D)^2}{\mathcal R_{\mathrm{hom}}^2}=1
 \quad\Longleftrightarrow\quad q_k=1\ \text{for all }k.
\]

If the \(q_k\) are not all one, then \(M>1\) and \(\mu\lambda>M\) for every finite irreducible generator.

**4. Attainability as an infimum.** For every \(\kappa>0\), take

\[
 D_\kappa=\kappa(v\mathbf 1_n^{\mathsf T}-I_n).
\]

Its off-diagonal rates are \(\kappa v_i>0\); it is conservative, irreducible and has stationary vector \(v\). The resolvent identity (using \((v\mathbf 1^{\mathsf T})^2=v\mathbf 1^{\mathsf T}\)) is

\[
 \mu(\mu I-D_\kappa)^{-1}
 =\frac{\mu}{\mu+\kappa}I_n
 +\frac{\kappa}{\mu+\kappa}v\mathbf 1_n^{\mathsf T}.
\]

As \(\kappa\to\infty\), the nonnegative matrix \(\mu K_{D_\kappa}\) converges to \(v\mathbf 1^{\mathsf T}L\). Spectral radius is continuous for finite matrices. The limit is rank one with sole possibly nonzero eigenvalue \(\mathbf 1^{\mathsf T}Lv\). Direct substitution shows

\[
 \mathbf 1^{\mathsf T}Lv=\sum_kh_k\left(\sum_i p_{ki}v_i/s_i\right)^2=M.
\]

The universal lower bound from Step 2 and this limiting construction prove the asserted exact infimum. For \(n=1\), \(r_1=q_k=M=1\) and the conclusion is immediate. This proves the theorem.

**5. Exact unequal-exposure example.** For \(m=n=2\), choose

\[
 h=(1/2,1/2),\quad P=\begin{pmatrix}3/4&1/4\\1/4&3/4\end{pmatrix},\quad v=(3/4,1/4)^{\mathsf T},\quad\mu=1.
\]

Then \(s=(1/2,1/2)\), \(q=(5/4,3/4)\), \(M=17/16\), and

\[
 L=\frac1{16}\begin{pmatrix}15&9\\3&5\end{pmatrix}.
\]

For \(D_\kappa\) above,

\[
 K_{D_\kappa}=\frac{1}{32(\kappa+1)}
 \begin{pmatrix}3(9\kappa+10)&3(7\kappa+6)\\3(3\kappa+2)&7\kappa+10\end{pmatrix}.
\]

Its characteristic polynomial, evaluated at \(17/16\), is exactly \(-3/[256(\kappa+1)]<0\), proving strict inequality at every finite \(\kappa>0\). At \(\kappa=1\) the Perron eigenvalue is \((37+\sqrt{985})/64>17/16\); it converges to \(17/16\) as \(\kappa\to\infty\).

## Verification

The proof does not depend on finite numerical experiments. The included `verify.py` uses exact rational arithmetic to reconstruct the two-group example from the defining matrices, verify its exact characteristic polynomial at four finite positive migration intensities, check the all-rate rational polynomial identity, and check the limiting variance floor. Execute `python3 verify.py` using only the Python standard library; the expected exit message is `VERIFY_OK`. This is a finite check of the illustrative algebra, **not** an exhaustive test of arbitrary dimensions, an infinite theorem prover, or an independent audit. The inequalities in Steps 1–4 are the proof for all admissible dimensions and generators.

## Relationship to prior work

Gao and Yuan [1, equation (4.4), Theorem 4.2 and Corollary 4.4] derive the matrix formula and the movement-independent baseline lower bound. **Their proof of Theorem 4.2 already includes a groupwise Cauchy–Schwarz inequality whose intermediate expression is the second moment \(M\)**; that intermediate inequality alone is not claimed here as a new discovery. Their discussion explicitly asks for a necessary and sufficient equality criterion in homogeneous environments, and Remark 4.8 exhibits equality with unequal patchwise host and vector shares. The additional mathematical statement here identifies the **sharp infimum over all finite vector migration generators with a fixed stationary distribution**, proves its nonattainment unless group exposures balance, and classifies the entire equality locus by the group exposures \(q_k\). The time-scale construction and equality rigidity are essential parts of this result.

Gao, van den Driessche and Cosner [2] establish an equality criterion for a different all-Eulerian host-and-vector migration model, namely aligned patchwise equilibrium populations. That stronger-looking spatial criterion does not cover the hybrid model, whose host groups retain residence labels. Gao and Cao [3] study both host and vector movement through Lagrangian residence matrices; the full manuscript was not obtained, and equivalence with a reduced model is a residual literature risk. The mathematical definition of that model does not contain the same variable conservative vector migration generator as here. A related later Eulerian host model [4] likewise involves different movement operators. The exact variational quantity in this theorem is not asserted to be the first possible variance inequality in all vector-borne epidemic models.

## Limitations

The result is specific to fixed \(P,h,v\) and homogeneous epidemiological parameters. It permits arbitrary finite vector migration rates, but no cap on their magnitude: if \(M>1\), the infimum is never achieved by a finite irreducible generator and is attained only in the fast-migration limit. Fixing a rate budget, graph topology, or detailed balance constraint is a different optimization problem. The theorem concerns \(\mathcal R_0\), not the equilibrium prevalence, epidemic trajectory, movement-cost tradeoff, or robustness to heterogeneous biting, recovery, vector mortality or incubation delays. A full-text comparison with [3] remains unavailable; absence from the searches conducted is not a general proof of novelty. Independent review has not been performed.

## References

1. D. Gao and X. Yuan, *A hybrid Lagrangian–Eulerian model for vector-borne diseases*, Journal of Mathematical Biology 89, article 16 (first published June 18, 2024). DOI: https://doi.org/10.1007/s00285-024-02109-5. Sections 2, 3, 4 (Theorem 4.2, Corollary 4.4, Remarks 4.7–4.8) and 6.
2. D. Gao, P. van den Driessche and C. Cosner, *Habitat fragmentation promotes malaria persistence*, Journal of Mathematical Biology (2019). Author-hosted manuscript: https://www.math.miami.edu/~dzgao/GvdDC-JMB2019.pdf. Theorem 3 and Corollary 1.
3. D. Gao and L. Cao, *Vector-borne disease models with Lagrangian approach*, Journal of Mathematical Biology 88, article 22 (2024). DOI: https://doi.org/10.1007/s00285-023-02044-x. Abstract and publicly available preview consulted; full text unavailable.
4. D. Gao and Y. Lou, *Effect of host movement on the prevalence of vector-borne diseases*, Journal of Mathematical Biology (2025), DOI: https://doi.org/10.1007/s00285-025-02254-5. Separate all-Eulerian host movement formulation.
