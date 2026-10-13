# An exact Haar law for two-qubit entanglement death under amplitude damping

## Finding

For two independent identical zero-temperature amplitude-damping channels acting on a complex Haar-random pure two-qubit input, the probability of retaining nonzero entanglement at any channel visibility \(0<q\leq1\) is exactly
\[
\boxed{\mathcal S(q)=\frac{1}{2[1+(1-q)^2]}+\frac{\arctan(1-q)}{2(1-q)}.}
\]
The second summand is defined by continuity at \(q=1\). With the Markovian visibility \(q=e^{-\gamma t}\), \(\gamma>0\), this is the survival function of the entanglement-death time \(T\): \(\Pr(T>t)=\mathcal S(e^{-\gamma t})\) for every finite \(t\geq0\). It includes an exact atom at infinity,
\[
\Pr(T=\infty)=\frac{2+\pi}{8},\qquad
\Pr(T<\infty)=\frac{6-\pi}{8}.
\]
In particular, as \(t\to\infty\),
\[
\Pr(T>t)=\frac{2+\pi}{8}+\frac{\pi}{8}e^{-\gamma t}+O(e^{-2\gamma t}),
\]
whereas at small positive times, \(\Pr(T\leq t)=\frac23\gamma^2t^2+O(t^3)\). These are properties of the same exact lifetime distribution, not separate optimization claims.

## Assumptions and scope

The ordered computational basis is \((|00\rangle,|01\rangle,|10\rangle,|11\rangle)\). A pure input is \(|\psi\rangle=a|00\rangle+b|01\rangle+c|10\rangle+d|11\rangle\) with \(|a|^2+|b|^2+|c|^2+|d|^2=1\), sampled from invariant complex Haar measure on the unit sphere of \(\mathbb C^4\). The two channels act independently, with identical Kraus operators
\[
K_0=|0\rangle\langle0|+\sqrt q\,|1\rangle\langle1|,\qquad K_1=\sqrt{1-q}\,|0\rangle\langle1|.
\]
The output state is \(\rho_q=(\mathcal A_q\otimes\mathcal A_q)(|\psi\rangle\langle\psi|)\). Entanglement means nonseparability of this two-qubit output, equivalent to positive Wootters concurrence. In the Markovian interpretation \(q(t)=e^{-\gamma t}\), define \(T=\inf\{t\ge0:\rho_{q(t)}\text{ is separable}\}\), with \(\inf\varnothing=\infty\). No assumptions about symmetry, real amplitudes, initial concurrence or excitation number are imposed.

## Proof

**Step 1: the exact statewise threshold.** Write the four unnormalized Kraus output vectors as \(v_{ij}=(K_i\otimes K_j)|\psi\rangle\). They are explicitly
\[
\begin{aligned}
v_{00}&=(a,\sqrt q\,b,\sqrt q\,c,qd)^T,\\
v_{01}&=(\sqrt{1-q}\,b,0,\sqrt{q(1-q)}\,d,0)^T,\\
v_{10}&=(\sqrt{1-q}\,c,\sqrt{q(1-q)}\,d,0,0)^T,\\
v_{11}&=((1-q)d,0,0,0)^T.
\end{aligned}
\]
The output is \(\rho_q=\sum_{i,j}v_{ij}v_{ij}^{\dagger}\). Wootters's spin-flip method states that its concurrence is the positive part of the largest singular value of the complex symmetric matrix \(M_{rs}=v_r^T(\sigma_y\otimes\sigma_y)v_s\) minus its other three singular values. Reorder the Kraus labels as \((00,11,01,10)\). Up to irrelevant common signs, \(M\) is the direct sum of the two symmetric blocks
\[
\begin{pmatrix}-2q(ad-bc)&-q(1-q)d^2\\-q(1-q)d^2&0\end{pmatrix}
\quad\text{and}\quad
\begin{pmatrix}0&q(1-q)d^2\\q(1-q)d^2&0\end{pmatrix}.
\]
Put \(A=q|ad-bc|\) and \(B=q(1-q)|d|^2\). The singular values of the first block are \(\sqrt{A^2+B^2}+A\) and \(\sqrt{A^2+B^2}-A\); those of the second are \(B,B\). Their decreasing order starts with \(\sqrt{A^2+B^2}+A\), and the sum of all remaining values equals \(\sqrt{A^2+B^2}-A+2B\), regardless of the order of the three smaller values. Consequently, for every normalized pure input and \(0\le q\le1\),
\[
C(\rho_q)=2q\,[|ad-bc|-(1-q)|d|^2]_+.
\]
For \(q>0\) the output is entangled precisely when \(|ad-bc|>(1-q)|d|^2\). Since this inequality becomes weaker as \(q\) increases, entanglement never revives in forward Markovian time, establishing the asserted survival-time interpretation. Haar-random initial inputs are entangled almost surely, since \(ad-bc=0\) is a proper complex algebraic hypersurface of Haar measure zero.

**Step 2: integrate over all complex Haar inputs.** Let \(A_0,B_0,C_0,D_0\) be four independent standard circular complex Gaussian variables (squared magnitudes independent exponential random variables of mean one). The normalized vector \((A_0,B_0,C_0,D_0)/R_0\), with \(R_0^2=\sum|\cdot|^2\), is Haar. The inequality in Step 1 is homogeneous of degree two, so normalization cancels. Conditional on \((C_0,D_0)\), the determinant \(\Delta=A_0D_0-B_0C_0\) is a circular complex Gaussian with variance \(Y=|C_0|^2+|D_0|^2\), and hence \(\Pr(|\Delta|>u|D_0|^2\mid C_0,D_0)=\exp[-u^2|D_0|^4/Y]\), where \(u=1-q\).

Now \(Y\) has gamma shape two and rate one, and \(X=|D_0|^2/Y\) is independent of \(Y\) and uniformly distributed on \([0,1]\). Therefore
\[
\begin{aligned}
\Pr(C(\rho_q)>0)
&=\mathbb E_{X,Y}\bigl[e^{-u^2YX^2}\bigr]
=\int_0^1\frac{dx}{(1+u^2x^2)^2}\\
&=\frac1{2(1+u^2)}+\frac{\arctan u}{2u}.
\end{aligned}
\]
The identity at \(u=0\) follows by continuity, completing the exact distribution for every \(0<q\le1\).

**Step 3: endpoints and time asymptotics.** Substitution \(u\uparrow1\) gives \(\mathcal S(0+)=1/4+\pi/8\). Note that \(\mathcal S(0+)\) is the limiting survival probability for arbitrarily small *positive* \(q\); at exactly \(q=0\), the channel replaces both qubits by \(|00\rangle\) and all entanglement vanishes. The positive limiting fraction therefore counts input states with no *finite* entanglement-death time, not entanglement persisting at the infinite-time endpoint state. Taylor expansion of the displayed closed form gives \(\mathcal S(q)=(2+\pi)/8+(\pi/8)q+O(q^2)\) as \(q\downarrow0\), and \(\mathcal S(1-u)=1-(2/3)u^2+O(u^4)\) as \(u\downarrow0\). Substituting \(q=e^{-\gamma t}\) and \(u=1-e^{-\gamma t}\) establishes the two time expansions and the exact atom at infinity. All limits and probabilities refer to complex Haar measure and fixed positive \(\gamma\).

## Verification

Run `python3 verify.py` with the single documented dependency in `requirements.txt`. The checker reconstructs all four channel Kraus vectors, computes 400 independent two-qubit concurrences directly from the spin-flip spectrum and tests the equivalent PPT entanglement decision. It numerically compares the exact integral to midpoint quadrature at four parameter values and checks the Haar-frequency law at three visibility values using a seeded Gaussian ensemble. It also checks the expansions at two values of each endpoint. A successful replay prints `VERIFY_OK direct_concurrence_and_PPT=400 quadrature=4 Haar_ensemble=3 time_limits=4`. The analytic proof, not the sampled experiments, establishes the universal quantifiers and asymptotic constants.

## Relationship to prior work

Wootters established the exact two-qubit concurrence method. Almeida et al. reported entanglement sudden death under two independent amplitude-loss channels for a special two-component input family; Huang and Zhu formulated necessary-and-sufficient sudden-death criteria for general initial states. Shan et al. treated extended-Werner-like initial families. Jiang, Shi and Du reported analytic state-by-state disentanglement times for arbitrary pure inputs. Datta evaluated a different Haar statistic, negativity before noise. Knoll et al. investigated a qualitative effective-entanglement-breaking characterization of sudden death. The present statement evaluates a distinct invariant-measure probability over **all** complex pure two-qubit states, rather than a statewise threshold, a restricted family, or a noiseless entanglement moment. Earlier arbitrary-state threshold theorems provide an essential antecedent; the contribution assessed here is the explicit Haar integral and full death-time law, including its nonzero infinite-time atom and sharp endpoint expansions.

## Limitations

The law assumes independent **identical**, zero-temperature Markovian amplitude-damping channels and complex Haar-distributed initial pure states. It does not cover unequal noise rates, thermal excitation, mixed-state ensembles, colored reservoirs, higher-dimensional parties, entanglement after postselection, or trajectories conditioned on detector outcomes. The two-qubit concurrence criterion is specific to the stated system. The analogous formula elsewhere in the literature cannot be ruled out; the full texts of plausible older papers by Huang–Zhu and Jiang–Shi–Du were not accessible for comparison. Neither numerical agreement nor a negative literature search certifies publication priority.

## References

- W. K. Wootters, *Entanglement of Formation of an Arbitrary State of Two Qubits*, arXiv:quant-ph/9709029v1 (public 1997-09-12); Phys. Rev. Lett. 80, 2245 (1998).
- M. P. Almeida et al., *Experimental Observation of Environment-induced Sudden Death of Entanglement*, arXiv:quant-ph/0701184v1 (public 2007-01-25); Science 316, 579 (2007).
- J.-H. Huang and S.-Y. Zhu, *Necessary and sufficient conditions for the entanglement sudden death under amplitude damping and phase damping*, Phys. Rev. A 76, 062322 (2007), DOI:10.1103/PhysRevA.76.062322.
- C. J. Shan et al., *Entanglement dynamics of two-qubit system in different types of noisy channels*, arXiv:0808.3690v1 (public 2008-08-27).
- A. Datta, *On the negativity of random pure states*, arXiv:1004.1317v1 (public 2010-04-08).
- F.-J. Jiang, M.-J. Shi and J.-F. Du, *Entanglement Dynamics of Arbitrary Two-Qubit Pure States under Amplitude and Phase Damping Channels*, Chin. Phys. Lett. 28, 020308 (2011), DOI:10.1088/0256-307X/28/2/020308.
- L. T. Knoll et al., *Entanglement breaking channels and entanglement sudden death*, arXiv:1602.07196v1 (public 2016-02-23).
