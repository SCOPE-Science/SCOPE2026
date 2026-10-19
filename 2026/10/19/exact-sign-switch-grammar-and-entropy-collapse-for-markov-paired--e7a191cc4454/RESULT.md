# Exact sign-switch grammar and entropy collapse for Markov paired tent maps

## Finding
For each integer \(n\ge1\), let \(\kappa_n\in(0,1/2)\) be the unique solution of
\[
\kappa_n[2(1+\kappa_n)]^n=1,
\qquad \lambda_n=2(1+\kappa_n).
\]
For the symmetric paired tent map \(T_n=T_{\kappa_n,\kappa_n}\) defined below, record the signs \(s_j\in\{-,+\}\) of an orbit avoiding zero and its full backward orbit, and record the sign-switch indicators \(e_j=\mathbf1_{s_{j+1}\ne s_j}\). **A finite switch word is realized by a nonempty open interval of initial points if and only if any two occurrences of \(1\) are separated by at least \(n\) zero symbols** (equivalently, two switch positions have distance at least \(n+1\)). Each admissible sign word has a positive-measure realization in either chosen initial half.

Let \(\Sigma_n\) be the closure in \(\{-,+\}^{\mathbb N_0}\) of these orbit sign itineraries. Its entropy is exactly
\[
h_{\mathrm{top}}(\Sigma_n)=\log\rho_n,\qquad
\rho_n^n(\rho_n-1)=1,\quad \rho_n>1.
\]
As \(n\to\infty\), writing \(W\) for the positive Lambert function,
\[
\log\rho_n\sim\frac{W(n)}{n}
\sim\frac{\log n}{n}
\sim\frac{\log2\;\log\log(1/\kappa_n)}{\log(1/\kappa_n)}.
\]
In contrast, the magnitude of every defined branch derivative is \(\lambda_n\to2\). Thus the entropy of the macroscopic binary sign process tends to zero although the microscopic expansion rate stays bounded away from one.

## Assumptions and scope
For \(0<\kappa<1/2\), put \(\lambda=2(1+\kappa)\), and define the (discontinuous at zero) piecewise-affine map \(T_\kappa:[-1,1]\to[-1,1]\) by
\[
T_\kappa(x)=
\begin{cases}
\lambda(x+1)-1,&-1\le x\le-1/2,\\
-\lambda x-1,&-1/2<x<0,\\
0,&x=0,\\
1-\lambda x,&0<x\le1/2,\\
1+\lambda(x-1),&1/2<x\le1.
\end{cases}
\]
The endpoint values at the turning points agree between neighboring formulas. For symbolic coding remove the countable union of preimages of \(0\), of the turning points, and of endpoints if desired; the resulting set contains all the positive-measure cylinders used below. The theorem concerns the sign observation, not full topological conjugacy between the interval map and the binary subshift. The Markov parameters and full-map transfer spectra are known prior results [1,2].

## Proof
**1. Parameter and forced recovery.** The map \(\kappa\mapsto\kappa[2(1+\kappa)]^n\) increases strictly from zero to a value exceeding one on \((0,1/2)\); hence \(\kappa_n\) exists uniquely. The map is odd away from zero. Write \(I_+=(0,1)\), \(I_-=(-1,0)\), and \(J_+=(0,\kappa_n)\), \(J_-=(-\kappa_n,0)\). A crossing of the sign boundary can land only in \(J_+\) or \(J_-\). For every \(x\in J_+\), the orbit follows the positive half and satisfies
\[
T_n^j(x)=1-\lambda_n^j x\in I_+\quad(1\le j\le n),
\qquad T_n^n(J_+)=I_+.
\]
To verify branch membership, for \(1\le j<n\) the point obeys \(T_n^j(x)>1-\lambda_n^{j-n}\ge1-\lambda_n^{-1}>1/2\), so each subsequent branch is the outer positive branch. The first iterate uses the inner positive branch because \(J_+\subset(0,1/2)\). The final formula holds since \(\lambda_n^n\kappa_n=1\). By oddness the identical statement holds for \(J_-\). Thus after a switch, the next \(n\) transitions must preserve the new sign, proving the forbidden-block condition for every genuine orbit.

**2. Surjective hold and switch-recovery branches.** On the positive side the interval
\[
D_+=(0,1/\lambda_n)\subset I_+
\]
consists of holding states and \(T_n:D_+\to I_+\) is an affine bijection. Likewise
\[
H_+=(1/\lambda_n,1/2)\subset I_+
\]
consists of switching states, \(T_n:H_+\to J_-\) is an affine bijection, and \(T_n^{n+1}:H_+\to I_-\) is an affine bijection with \(n\) prescribed intermediate negative states. Negating the intervals gives the two analogous branches from \(I_-\). The construction therefore has a full onto branch for the marker block \(0\) of length one, and a full onto branch for \(10^n\) of length \(n+1\). Its Jacobian is everywhere nonzero.

Every finite binary word whose ones are \(n\)-separated is a concatenation of these blocks, possibly ending in a proper prefix of \(10^n\). Reading such a concatenation backwards with the full onto branches yields a nonempty open interval of starting states in either prescribed initial half; truncating the terminal block does not destroy positive length. Its orbit sign changes precisely at the prescribed marker positions. Hence the forbidden-block condition is also sufficient, with positive-Lebesgue-measure cylinders. This statement includes all finite boundary cases, such as a switch at the final observed transition.

**3. Entropy.** Let \(a_m\) count marker words of length \(m\). For \(0\le m\le n\), \(a_m=m+1\), since at most one marker can occur. For all \(m\ge n+1\), classification by the first symbol gives
\[
a_m=a_{m-1}+a_{m-n-1}.
\]
The associated primitive finite-state presentation has Perron root \(\rho_n>1\) determined by \(\rho_n^{n+1}=\rho_n^n+1\). A sign word of length \(m+1\) is uniquely determined by its first sign and its \(m\) marker bits. Thus the number of sign words is exactly \(2a_m\), and the exponential growth rate is \(\log\rho_n\). This defines the topological entropy of the sign-itinerary closure, without assigning entropy to the countable excluded boundary orbits.

**4. Asymptotics.** Since \(\kappa_n\le2^{-n}\), we have \(n\kappa_n\to0\), and consequently
\[
\kappa_n=2^{-n}(1+\kappa_n)^{-n}\sim2^{-n}.
\]
Put \(\delta_n=\rho_n-1\), so \(\delta_n(1+\delta_n)^n=1\). Then \(\delta_n\to0\); setting \(u_n=n\delta_n\), one has \(u_ne^{u_n}=n(1+o(1))\) with a relative error tending to zero because \(u_n=O(\log n)\). Hence \(u_n\sim W(n)\), and \(\log\rho_n\sim W(n)/n\sim(\log n)/n\). Inserting \(n\sim\log(1/\kappa_n)/\log2\) proves the claimed small-leak expression. Finally \(\lambda_n=2(1+\kappa_n)\to2\).

## Verification
A standalone standard-library diagnostic (`verify.py`) reconstructs each Markov parameter by bisection for \(1\le n\le6\), checks the crossing/recovery branch conditions and entropy polynomial, and exhaustively compares finite sign-cylinder realizability against the stated forbidden-block grammar for all sign words through length ten. It separately compares the word counts with the renewal recurrence. The program passed **12,276 finite sign-word comparisons**. This finite experiment supports boundary handling and implementation but is **not** the proof for arbitrary \(n\) or infinite sequences; Steps 1–4 supply that proof.

## Relationship to prior work
Horan [1] publicly introduced the same special Markov parameter sequence, its partition and its full Perron–Frobenius spectral problem; these facts are prior, not new. Horan's further determinant-free study [2] determines full-map spectral information and the spectrum of a distinct magnitude quotient. González-Tokman and Peters [3] study random perturbations, invariant-density averaging and Oseledets limits for the larger paired-tent family. The present claim is restricted to **the exact sign-switch language and its entropy for this deterministic sequence**, and a quantified loss of symbolic entropy under that coarse observation. It does not claim the classical no-nearby-ones shift, renewal recurrence, Lambert asymptotic or Markov construction individually as new. Those ingredients arise in the proof; the stated factor identification is the proposed contribution.

## Limitations
This is a deterministic one-parameter sequence rather than arbitrary asymmetric or randomly forced paired-tent maps. It describes the topological language of an observation, not physical sign-process probabilities, mixing times or Shannon entropy under the invariant density. Zero-hitting and turning-point preimages are excluded when coding; their countable exceptional set is not assigned sign symbols. Earlier full Markov partitions could allow an equivalent symbolic-factor result to be reconstructed, so historical priority remains subject to further verification.

## References
[1] J. Horan, *Asymptotics for the second-largest Lyapunov exponent for some Perron–Frobenius operator cocycles*, arXiv:1910.12112v1, 2019-10-26, §4.6, https://arxiv.org/abs/1910.12112.

[2] J. Horan, *Dynamical spectrum via determinant-free linear algebra*, arXiv:2001.06788, 2020, https://arxiv.org/abs/2001.06788; and *Spectral gap and asymptotics for a family of cocycles of Perron–Frobenius operators*, University of Victoria PhD dissertation, 2020, Chapter 5, https://dspace.library.uvic.ca/bitstreams/8562f6eb-cc75-497a-8f7f-299b114ec884/download.

[3] C. González-Tokman and J. Peters, *Averaging for random metastable systems*, arXiv:2406.09672v1 (2024-06-14), §8, https://arxiv.org/abs/2406.09672.
