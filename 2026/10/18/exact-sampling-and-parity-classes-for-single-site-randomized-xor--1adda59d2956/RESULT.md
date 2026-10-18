# Exact sampling and parity classes for single-site randomized XOR shift registers

## Finding
Fix any integer \(n\ge1\) and a site \(1\le j\le n\). In \(V=\mathbb F_2^n\), let
\[
 A(x_1,\ldots,x_n)=(x_2,\ldots,x_n,x_1+\cdots+x_n),
 \qquad X_{t+1}=A(X_t+B_{t+1}e_j),
\]
where all sums are in \(\mathbb F_2\), the \(B_t\) are independent fair bits, and \(X_0=x\) is an arbitrary fixed state. The uniform measure \(\pi\) on \(V\) is stationary. Define \(g=\gcd(j,n+1)\) and \(r_t=\min\{t,n+1-g\}\) for integers \(t\ge0\).

**Exact distribution and distance theorem.** At every \(t\), \(X_t\) is uniform on an affine space of \(2^{r_t}\) states, and
\[
 \boxed{\|\mathcal L_x(X_t)-\pi\|_{\rm TV}=1-2^{r_t-n}.}
\]
Thus this chain produces an exact uniform sample for the first time at \(t=n\) if and only if \(\gcd(j,n+1)=1\). Otherwise it never converges to the full uniform law, and its distance is exactly \(1-2^{1-g}\) for every \(t\ge n+1-g\).

**Communication-class theorem.** If \(g>1\), the chain has deterministic quotient evolution given by cyclic rotation of an even-parity binary word of length \(g\). Its closed irreducible classes are in bijection with rotation orbits of such words. A class corresponding to an orbit of size \(\ell\) has period \(\ell\), and the number of classes is
\[
 C_g=\frac1g\sum_{s=0}^{g-1} F_g(s),\qquad
 F_g(s)=\begin{cases}
 2^{d_s},&g/d_s\text{ is even},\\
 2^{d_s-1},&g/d_s\text{ is odd},
 \end{cases}\quad d_s=\gcd(g,s),
\]
with the convention \(\gcd(g,0)=g\). For \(g=1\) there is one aperiodic class. For example, \(n=8,j=3\) has \(g=3\) and permanent total variation distance \(3/4\), whereas \(j=4\) produces an exact uniform state at time eight.

## Assumptions and scope
The state space is the full \(n\)-dimensional binary vector space, the injected coordinate is fixed in time, and the injected bits are **independent and fair**. Each step injects the bit *before* applying \(A\). The stated total variation distance is to the full uniform stationary distribution, not to the class-conditional law. The results hold for every starting point, integer time, site, and positive dimension, including \(n=1\).

## Proof
**1. Invertibility and representation.** The last output coordinate of \(A\), together with the first \(n-1\) output coordinates, determines the omitted first input coordinate. Hence \(A\) is invertible, and both bit addition and \(A\) preserve uniform measure. Expanding the recursion gives
\[
 X_t=A^tx+\sum_{k=1}^{t} B_k A^{t-k+1}e_j.
\]
Thus the support is an affine translate of
\(W_t=\operatorname{span}_{\mathbb F_2}\{Ae_j,A^2e_j,\ldots,A^te_j\}\); its distribution is uniform because a linear map sends uniform independent bits to the uniform law on its image. It remains to calculate \(\dim W_t\).

**2. A cyclic edge conjugacy.** Write \(m=n+1\), and put \(b_s=A^se_1\) for \(0\le s\le n\). Direct calculation yields
\[
 b_0=e_1,\quad b_1=e_n,\quad
 b_s=e_{n-s+1}+e_{n-s+2}\quad(2\le s\le n),
\]
where the final range is empty when \(n=1\). In particular \(b_0,\ldots,b_{n-1}\) form a basis, \(\sum_{s=0}^{n}b_s=0\), and \(Ab_n=b_0\); equivalently \(A^m=I\). To see the last assertion without any extrapolation, the displayed basis elements verify the periodic orbit by direct substitution into the defining rule for \(A\).

Let \(H_0=\{y\in\mathbb F_2^{m}:\sum_{a=0}^{m-1}y_a=0\}\), with canonical basis \(E_0,\ldots,E_{m-1}\) in the ambient space, and let \(R E_a=E_{a+1\bmod m}\). The edge vectors \(E_s+E_{s+1}\) for \(0\le s\le n-1\) form a basis of \(H_0\). Hence a unique linear isomorphism \(\Phi:V\to H_0\) takes \(b_s\) to \(E_s+E_{s+1}\). The relations above and the vanishing sum over the complete cycle give \(\Phi A=R\Phi\).

Since \(e_j=\sum_{s=1}^{n-j+1}b_s\) (the sum telescopes),
\[
 \Phi(e_j)=E_1+E_{n-j+2\bmod m}=E_1+E_{1-j\bmod m}.
\]
Therefore the noise directions \(\Phi(A^ke_j)\), \(k=1,\ldots,t\), are consecutive cyclic translates of an edge whose endpoints differ by \(j\) modulo \(m\).

**3. Exact graph rank.** On \(\mathbb Z_m\), connect \(a\) to \(a-j\) for every \(a\). This graph is the disjoint union of \(g=\gcd(j,m)\) cycles, one in each residue class modulo \(g\), each of size \(m/g\); a two-vertex component may be viewed as having two directed occurrences of the same undirected edge. The first \(m-g=g(m/g-1)\) consecutive edge occurrences comprise exactly \(m/g-1\) edges from each cycle, and therefore form a forest. Indeed, each residue class appears exactly \(m/g-1\) times among \(m-g\) consecutive integer indices. Hence the first \(t\le m-g\) edge incidence vectors are linearly independent over \(\mathbb F_2\). All remaining edges belong to the span of the forest, as each cycle has only \(m/g-1\) independent incidence directions. The resulting formula is
\[
 \dim W_t=\min(t,m-g)=r_t.
\]

**4. Total variation and the sharp dichotomy.** If \(\nu\) is uniform on a nonempty subset of size \(2^r\) of an \(n\)-dimensional binary space, then direct summation gives
\(\|\nu-\pi\|_{\rm TV}=1-2^{r-n}\). This proves the stated exact profile. Because \(j\in\{1,\ldots,n\}\), \(g<m\) and \(m-g\le n\), with equality precisely for \(g=1\). Consequently only coprime sites can yield the whole uniform law, first at step \(n\), while noncoprime sites plateau at the claimed distance.

**5. Recurrent classes and periods.** Let \(H\subset H_0\) be the full span of the cyclic edge directions. The map \(P:H_0\to\mathbb F_2^g\) records the parity of the coordinates in each of the \(g\) residue classes modulo \(g\). Graph incidence vectors show \(\ker P=H\) and \(\dim H=m-g\). Because vectors in \(H_0\) have even total parity, the image of \(P\) is exactly the even-parity subspace of \(\mathbb F_2^g\). Noise leaves \(P\) unchanged and \(R\) cyclically permutes its coordinates. Hence quotient paths rotate deterministically, and no two distinct rotation orbits communicate. Once \(t\ge m-g\), however, the law from every state is **uniform on the entire affine fiber** indexed by the rotated quotient word, by steps 1–3. Thus any state in the same rotation orbit can be reached in a sufficiently large permitted time, proving that each orbit gives precisely one irreducible closed class. Returns can occur only at multiples of the orbit length \(\ell\), and all sufficiently large such multiples have positive return probability; the class period is exactly \(\ell\).

Finally, Burnside's formula counts the rotation orbits. A length-\(g\) binary word fixed by rotation through \(s\) coordinates has \(d_s=\gcd(g,s)\) independent cycle values, each repeated \(g/d_s\) times. The even-parity restriction removes half the assignments if that repeat count is odd, and removes none if it is even. This gives \(F_g(s)\) and the class-count formula.

## Verification
The accompanying standalone `verify.py` uses only Python's standard library. It independently constructs the binary transition, checks binary ranks of the first \(t\) noise directions for every \(1\le n\le80\), every legal injection site, and every \(0\le t\le n+3\), and performs exact integer-probability enumeration for all \(n\le8\) from several distinct initial states. The run passed 186840 orbit-rank checks and 1039 full-state distribution checks. These finite checks support but do not replace the all-dimension graph-incidence proof above. Run with `python3 verify.py`.

## Relationship to prior work
Levin and Tankala [1, Section 5, Theorem 2] proved exact time-\(n\) uniformity for their related fixed-**middle**-coordinate chain when \(n=2m\); their principal theorem addresses random-coordinate updates. The present theorem uses their shift-register map but classifies **every** fixed injection site and dimension, supplies the **entire exact finite-time total-variation profile**, and identifies the arithmetic parameter separating exact sampling from nonergodicity. The middle site when \(n=2m\) has \(\gcd(m,2m+1)=1\), so their result is a special case. Diaconis and Graham [2] study affine hypercube walks with a different linear map and noise mechanism; generic Fourier/linear-algebra methods there do not state the specific cyclic-graph rank or parity-class decomposition here. Chung, Diaconis, and Graham [4] analyze affine walks on integers modulo an odd modulus with random \(0,1,-1\) offsets, a different setting.

## Limitations
The conclusions require fair independent inserted bits and one fixed insertion site; switching sites, biased noise, or a different feedback polynomial need separate analysis. Full uniformity is stationary even in the nonergodic cases, but the law from one deterministic start then fails to approach that stationary measure. The conclusions are mathematical deductions of the specified model, not a claim of historical priority certified against all coding-theory or linear-control literature. Equivalent older language about cyclic vectors or controllability could cover parts of the classification and remains a documented novelty risk.

## References
[1] D. A. Levin and C. Tankala, *Fast mixing of a randomized shift-register Markov chain*, arXiv:2109.05387v1 (first public September 11, 2021), *Journal of Applied Probability* **60** (2023), 253–266, doi:10.1017/jpr.2022.37. Full text: https://arxiv.org/pdf/2109.05387.

[2] P. Diaconis and R. L. Graham, *An affine walk on the hypercube*, *Journal of Computational and Applied Mathematics* **41** (1992), 215–235. Author-available text: https://fanchung.ucsd.edu/ron/papers/92_01_hypercube_walk.pdf.

[3] A. Ben-Hamou and Y. Peres, *Cutoff for permuted Markov chains*, arXiv:2104.03568 (2021). Cited for contextual comparison only; the full document was not accessible for a complete theorem-by-theorem comparison.

[4] F. R. K. Chung, P. Diaconis, and R. L. Graham, *Random walks arising in random number generation*, *Annals of Probability* **15** (1987), 1148–1165. Author-available text: https://fanchung.ucsd.edu/mypaps/fanpap/88walks.pdf.
