# Three exact additive-commutator fibers distinguish the central series of \(\mathfrak n_4(\mathbb F_q)\)

## Finding

Let \(q\) be any prime power. In the six-dimensional algebra \(N=\mathfrak n_4(\mathbb F_q)\) of strictly upper triangular \(4\times4\) matrices, use the **additive algebra commutator** \([X,Y]=XY-YX\), and for every target \(Z\) define
\[
F_q(Z)=\#\{(X,Y)\in N^2:[X,Y]=Z\}.
\]
All outputs are in the three-dimensional Lie derived space \([N,N]=\langle E_{13},E_{24},E_{14}\rangle\). For \(Z=uE_{13}+vE_{24}+wE_{14}\), the exact answer is
\[
\boxed{F_q(Z)=
\begin{cases}
2q^9+q^8-2q^7,&u=v=w=0,\\
2q^9-2q^7,&u=v=0,\ w\ne0,\\
q^9-q^7,&(u,v)\ne(0,0).
\end{cases}}
\]
The three values occur at \(1\), \(q-1\), and \(q^3-q\) targets respectively, and every element of \([N,N]\) occurs as an individual commutator. In particular, among nonzero outputs, the fiber function **recovers the center of the derived series**: \([N,[N,N]]=Z(N)=\langle E_{14}\rangle\) is precisely the line whose nonzero elements have twice the generic nonzero fiber count. This is the first non-Heisenberg unitriangular size and gives an exact finite-field benchmark for the effect of the third lower-central layer on a bilinear commutator distribution.

## Assumptions and scope

The field \(\mathbb F_q\) can have any positive characteristic, including \(2\), and may be a nonprime finite field. The algebra \(N\) is nonunital. Let \(E_{ij}\) denote the matrix unit, with \(1\le i<j\le4\). We count ordered pairs \((X,Y)\), including zero matrices, with the additive bracket; group commutators in \(1+N\) are a different word map. By convention, \([N,N]\) is the span of brackets and \([N,[N,N]]\) is the third lower-central term.

## Proof

Every matrix in \(N\) is uniquely
\[
X=aE_{12}+bE_{23}+cE_{34}+dE_{13}+eE_{24}+fE_{14},
\]
and similarly write \(Y=AE_{12}+BE_{23}+CE_{34}+DE_{13}+EE_{24}+FE_{14}\). Direct multiplication of matrix units gives the exact three coordinates
\[
[X,Y]=(aB-bA)E_{13}+(bC-cB)E_{24}
 +(aE-eA+dC-cD)E_{14}.
\]
Thus the image is contained in \([N,N]=\langle E_{13},E_{24},E_{14}\rangle\), while the brackets \([E_{12},E_{23}]=E_{13}\), \([E_{23},E_{34}]=E_{24}\), \([E_{12},E_{24}]=E_{14}\) show this is exactly the derived space. These same brackets show \([N,[N,N]]=\langle E_{14}\rangle\); commuting with each matrix unit shows \(Z(N)=\langle E_{14}\rangle\).

Fix a nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C^\times\) and a dual functional \(\lambda=(\alpha,\beta,\gamma)\in[N,N]^*\) in the displayed basis. Its alternating bilinear form is
\[
B_\lambda(X,Y)=\alpha(aB-bA)+\beta(bC-cB)
+\gamma(aE-eA+dC-cD).
\]
The rank \(r_\lambda\) of \(B_\lambda\) is
\[
r_\lambda=
\begin{cases}
0,&\alpha=\beta=\gamma=0,\\
2,&\gamma=0,\ (\alpha,\beta)\ne(0,0),\\
4,&\gamma\ne0.
\end{cases}
\]
Indeed, in the middle case the restriction to \(a,b,c\) is a nonzero alternating form on a three-space, hence rank \(2\). If \(\gamma\ne0\), the independent pairings between \(a,e\) and \(d,c\) give an invertible alternating \(4\times4\) minor; the form is supported on only five of the six variables (\(f\) never appears), and every alternating form on an odd-dimensional space has even rank, so its rank is exactly \(4\). These arguments also hold in characteristic \(2\), because alternating means \(B_\lambda(X,X)=0\).

For each fixed \(X\), the character sum over \(Y\) is \(q^6\) when \(X\) belongs to the radical of \(B_\lambda\), and zero otherwise. The radical has dimension \(6-r_\lambda\); therefore the **exact**, not asymptotic, double character sum is
\[
S(\lambda)=\sum_{X,Y\in N}\psi(B_\lambda(X,Y))=q^{12-r_\lambda}.
\]
Fourier inversion on the three-dimensional additive group \([N,N]\) yields for \(Z=(u,v,w)\)
\[
F_q(Z)=q^{-3}\left[q^{12}
 +q^{10}\sum_{(\alpha,\beta)\ne(0,0)}
\psi(-\alpha u-\beta v)
 +q^8\sum_{\gamma\ne0}\sum_{\alpha,\beta\in\mathbb F_q}
\psi(-\alpha u-\beta v-\gamma w)\right].
\]
The first finite sum is \(q^2-1\) when \((u,v)=0\), and \(-1\) otherwise. The second sum is \(q^2(q-1)\) for \((u,v,w)=0\), is \(-q^2\) for \((u,v)=0\) and \(w\ne0\), and is \(0\) when \((u,v)\ne0\). Substitution proves exactly the three displayed fiber formulas with no excluded field sizes or characteristics.

Every fiber value is positive. Since the remaining \(q^6-q^3\) matrices outside \([N,N]\) have empty fibers, the set of individual additive commutators equals \([N,N]\). Summing the three values with multiplicities \(1,q-1,q^3-q\) gives exactly \(q^{12}\), independently checking normalization. The nonzero fiber ratio \((2q^9-2q^7)/(q^9-q^7)=2\), and these two nonzero values are distinct, proving the asserted center detection.

As a separate zero-fiber cross-check, the linear adjoint map \(\operatorname{ad}_X:Y\mapsto[X,Y]\) has rank distribution \(r=0,1,2,3\) with multiplicities, respectively,
\[
q,\qquad q(q^2-1),\qquad q^3(q^2+q-2),\qquad q^3(q-1)(q^2-1).
\]
This follows by examining its columns: with output coordinates \((E_{13},E_{24},E_{14})\), the nonzero candidate columns are \((-b,0,-e)\), \((a,-c,0)\), \((0,b,d)\), \((0,0,-c)\), \((0,0,a)\). If \(b\ne0\) and \((a,c)\ne0\), the rank is \(3\); if \(b\ne0\) and \(a=c=0\) it is \(2\); if \(b=0\) and \((a,c)\ne0\) it is \(2\); and when \(a=b=c=0\) its rank is \(1\) unless also \(d=e=0\), when it is \(0\). Thus \(\sum_X |\ker\operatorname{ad}_X|=\sum_{r=0}^3N_rq^{6-r}=2q^9+q^8-2q^7\), consistent with the Fourier evaluation. The commuting-pair probability is \((2q^2+q-2)/q^5\); this last **zero-target** quantity is not asserted as a novel standalone result.

## Verification

The included standalone `artifacts/verify.py` runs using standard Python 3 only. It enumerates all ordered pairs directly by multiplying two \(4\times4\) matrices over \(\mathbb F_2\) and \(\mathbb F_3\), verifying **every** target fiber and normalization without using the bracket-coordinate formula. It separately enumerates the images and kernels of all \(q^6\) adjoint maps for \(q=4,5\), using \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\), and checks every target, the exact rank histogram, and the total \(q^{12}\) pairs. The complete replay prints `VERIFY_OK`.

The reported field checks, though exhaustive for their own finite fields, do **not** prove the all-prime-power theorem; the character-rank proof above does that.

## Relationship to prior work

Eberhard studies commuting probabilities of finite groups and proves broad structural results for zero fibers of general bilinear maps, supplying a natural finite-field commutator-count motivation. Soffer studies commuting pairs in strictly upper triangular algebras through unitriangular-group conjugacy and bounds. Those methods concern the *zero* bracket fiber and more general asymptotic behavior; the specific complete three-valued **nonzero target** distribution is not asserted there. The general Fourier-rank technique, the identification of \(\mathfrak n_4\), and the classical zero-fiber computation are background, not claimed inventions.

The related result titled *Commutator fibers and commuting probabilities of finite Kronecker path algebras* treats a two-vertex radical-square-zero algebra whose nonzero radical commutators have a single common fiber. It does not imply the present characteristic-free **two-level nonzero fiber** distinction in a class-three nilpotent triangular algebra. A separate exact result for prescribed commutator graphs of \(M_2(\mathbb F_q)\) uses the trace pairing in the full matrix ring, also not this algebra or fiber function. The previously studied full upper triangular \(T_3(\mathbb F_q)\) has a different algebra and four target strata; it does not imply this three-stratum census.

There is a closely related literature on *group* commutator-word distributions in unitriangular groups. A group commutator is not the additive map \((X,Y)\mapsto XY-YX\). Any algebra-to-group distribution transfer would require proof and is not presumed absent simply because terminology differs.

## Limitations

The theorem addresses exactly \(4\times4\) strictly upper triangular matrices and only the additive Lie commutator. It neither gives a general \(n\)-uniform formula nor claims that distinct target fibers characterize arbitrary nilpotent Lie algebras. It uses a classical character-sum method and contains the already-known zero-fiber value as a necessary normalization, not as a new achievement. Literature coverage is not complete: an equivalent finite-size fiber table or a general formula implying it may occur under a different terminology, including group-algebra correspondences.

## References

1. S. Eberhard, *Commuting probabilities of finite groups*, arXiv:1411.0848v1 (first public 4 November 2014; primary MSC 20D60), https://arxiv.org/abs/1411.0848 .
2. A. Soffer, *Upper bounds on the number of conjugacy classes in unitriangular groups*, arXiv:1411.5389v1 (first public 19 November 2014), https://arxiv.org/abs/1411.5389 .
3. *Commutator fibers and commuting probabilities of finite Kronecker path algebras*, published finite-field path-algebra result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-commutator-fibers-and-commuting-probabilities-of-finite-kronecke--75cb49b6c27d .
4. *Degree distribution of prescribed-commutator graphs of two-by-two matrix rings*, published finite-field matrix-ring result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-degree-distribution-of-prescribed-commutator-graphs-of-two-by-tw--5edf6ac2ab3b .
