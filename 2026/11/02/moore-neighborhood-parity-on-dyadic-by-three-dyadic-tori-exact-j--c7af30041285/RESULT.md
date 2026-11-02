# Moore-neighborhood parity on dyadic-by-three-dyadic tori: exact Jordan chains and orbit populations

## Finding

For any integers \(a\ge 2\), \(b\ge0\), put \(M=2^a\), \(d=2^b\) and \(N=3d\). Over an arbitrary finite field \(K=\mathbb F_q\) of characteristic two, let \(T\) be synchronous XOR-sum over the eight distinct Moore neighbors of each site of the torus \(\mathbb Z/M\mathbb Z\times\mathbb Z/N\mathbb Z\). Define \(L=\max(M,d)/2\) and \(c=2\min(M,d)\).

The complete Jordan decomposition, over the ground field itself, is
\[
T\sim J_L(0)^{\oplus c}\oplus J_d(1)^{\oplus 2M}.
\]
In particular the longest transient before a configuration becomes periodic is exactly \(L\), while the order of the dynamics restricted to its periodic configurations is exactly \(d\), independently of \(M\). When \(b=0\), every periodic configuration is fixed (even as the zero-primary transient length \(M/2\) grows). For \(b\ge1\), every power-of-two period \(1,2,4,\ldots,d\) is realized and no other primitive period exists.

Let \(E(x)\) denote the first nonnegative iterate for which \(T^{E(x)}x\) is periodic. For every \(0\le t\le L\),
\[
\#\{x:E(x)\le t\}=q^{2Md+ct}.
\]
Thus the exact initial-entry counts are \(q^{2Md}\) for \(t=0\) and \(q^{2Md+ct}-q^{2Md+c(t-1)}\) for \(1\le t\le L\).

For \(j=0,\ldots,b\), define \(p_j=2^j\) and
\[
P_j=\begin{cases}q^{2M},&j=0,\\
q^{2M2^j}-q^{2M2^{j-1}},&1\le j\le b.\end{cases}
\]
Then \(P_j\) is the exact number of periodic configurations with primitive period \(p_j\), and \(P_j/p_j\) is the number of primitive periodic orbits. More sharply, with \(A_0=1\) and \(A_t=q^{ct}-q^{c(t-1)}\) for \(1\le t\le L\), the number of initial states whose first periodic entry is \(t\) and whose eventual primitive period is \(p_j\) equals \(A_tP_j\). These formulas exhaust the \(q^{3Md}\) initial configurations.

## Assumptions and scope

The torus has periodic boundary conditions in both axes; its dimensions satisfy \(M\ge4\) and \(N\ge3\), so the eight displacement vectors \((\epsilon,\delta)\in\{-1,0,1\}^2\setminus\{(0,0)\}\) specify distinct neighbors. The update sums all eight neighboring values, excludes the central site's value, and acts synchronously. The field has \(q=2^h\), \(h\ge1\). The claimed similarity is over \(\mathbb F_q\), not merely over an algebraic closure. Jordan blocks \(J_r(\lambda)\) have size \(r\) and eigenvalue \(\lambda\).

## Proof

**1. Convolution and the two cyclotomic components.** Let
\[
R=K[x^{\pm1},y^{\pm1}]/(x^M-1,y^{3d}-1).
\]
With site states identified with its standard monomial basis, \(T\) is multiplication by
\[
F=(1+x+x^{-1})(1+y+y^{-1})+1
  =(x+x^{-1})+(y+y^{-1})+(x+x^{-1})(y+y^{-1}).
\]
The first expression has the central coefficient canceled in characteristic two and hence exactly the eight prescribed neighbor terms. Write \(s=x+x^{-1}\), \(t=y+y^{-1}\), so \(F=s+t+st\).

Since \(M\) and \(d\) are powers of two,
\[
x^M-1=(x+1)^M,\qquad y^{3d}-1=(y+1)^d(y^2+y+1)^d.
\]
The latter two factors are relatively prime over every characteristic-two field, whether or not it contains a primitive third root of unity. The Chinese remainder theorem therefore decomposes the \(y\)-ring into its \((y+1)\)-primary component \(A\) of dimension \(d\) and its \((y^2+y+1)\)-primary component \(B\) of dimension \(2d\). The resulting decomposition of \(R\) is invariant under multiplication by \(F\).

**2. Nilpotent component.** In the \(x\)-ring write \(u=x+1\). As \(x=1+u\),
\[
s=(1+u)+(1+u)^{-1}=\frac{u^2}{1+u}.
\]
The elements \(s^i\) and \(u s^i\), for \(0\le i<M/2\), have distinct leading \(u\)-degrees \(2i\) and \(2i+1\); they form a \(K\)-basis. Thus \(R_x\) is free of rank two over \(K[s]/(s^{M/2})\). For \(d\ge2\), the analogous substitution \(v=y+1\) in \(A\) gives \(t=v^2/(1+v)\); \(A\) is free of rank two over \(K[t]/(t^{d/2})\). Consequently \(R_x\otimes A\) is free of rank four over
\[
H=K[s,t]/(s^{M/2},t^{d/2}),
\]
and multiplication by \(F\) acts as multiplication by \(z=s+(1+s)t\) on each copy.

Put \(p=M/2\), \(r=d/2\), both powers of two. If \(r\ge p\), fix \(s\) and replace the coordinate \(t\) by \(z=s+(1+s)t\). This is an invertible triangular substitution with inverse \(t=(z+s)/(1+s)\); its defining relations are \(s^p=z^r=0\), because \(z^r=s^r+(1+s)^rt^r=0\). Conversely \(t^r=(z+s)^r/(1+s)^r=0\). If \(p\ge r\), instead fix \(t\) and replace \(s\) by \(z=t+(1+t)s\), with inverse \(s=(z+t)/(1+t)\), to obtain relations \(t^r=z^p=0\). In both cases, \(H\) becomes a free module of rank \(\min(p,r)\) over \(K[z]/z^{\max(p,r)}\). Multiplication by \(z\) consequently has \(4\min(p,r)=2\min(M,d)=c\) Jordan chains, each of length \(\max(p,r)=L\).

For \(d=1\), the component \(A=K\) has \(y=1\) and \(t=0\), so \(F=s\) on \(R_x\). The same \(s\)-basis shows precisely two blocks \(J_{M/2}(0)\). This agrees with \(c=2\) and \(L=M/2\).

**3. Invertible component.** In \(B\), set
\[
w=1+t=\frac{y^2+y+1}{y}.
\]
The element \(y\) is a unit. Therefore \(w^d=0\), and multiplication by powers of \(w\) generates the same filtration as powers of the defining polynomial \(y^2+y+1\). Explicitly, \(B\) is free of rank two over \(K[w]/w^d\), with basis \(1,y\): the relation \(y^2+(1+w)y+1=0\) is monic, and its quotient has dimension \(2d\). On this component
\[
F=s+(1+s)(1+w)=1+(1+s)w.
\]
Since \(s\) is nilpotent, \(1+s\) is invertible in \(R_x\). The substitution \(w'=(1+s)w\) is thus invertible over \(R_x\) and preserves a free rank-two basis over the truncated \(w'\)-ring. The \(K\)-dimension of \(R_x\) is \(M\). Hence multiplication by \(F=1+w'\) on \(R_x\otimes B\) has exactly \(2M\) Jordan blocks \(J_d(1)\), with no splitting-field assumption. Combining the two invariant components proves the claimed Jordan decomposition. The dimensions add correctly: \(cL=Md\) and \(2Md+Md=3Md\).

**4. Population and period calculations.** A vector is eventually periodic exactly when its nilpotent-primary component vanishes; otherwise its first periodic entry is the first iterate killing that component. For \(0\le t\le L\), the nilpotent kernel has dimension \(c\min(t,L)\). Its direct product with the \(2Md\)-dimensional invertible component gives the first-entry counts.

On a length-\(d\) unipotent block \(U=I+J_d(0)\), characteristic two implies \(U^{2^j}=I+J_d(0)^{2^j}\). Thus the periodic component fixed by \(T^{2^j}\) has dimension \(2M\min(2^j,d)\), and there are \(q^{2M\min(2^j,d)}\) such states. Because every possible period divides \(d\), subtracting consecutive fixed-point populations gives \(P_j\); division by the orbit length gives the orbit count. Tensoring the independent nilpotent-entry layer with the invertible period class yields \(A_tP_j\). Every upper bound is attained because the listed Jordan blocks exist, and the formulas telescope to the whole state space.

## Verification

The self-contained `moore_verify.py` constructs the actual eight-neighbor binary adjacency matrices and independently checks nullities of successive powers of \(T\) and of \(T^{2^j}-I\). It verifies 15 distinct torus dimensions with \(M\in\{4,8,16,32\}\), \(d\in\{1,2,4,8\}\), and at most 384 sites. It also enumerates all \(4096\) binary configurations on the \(4\times3\) torus and checks that first-periodic-entry counts are \(256\), \(768\), \(3072\) for times zero, one, two, respectively. The captured output ends with `ALL_TESTS_PASSED cases= 15`. Run `python3 moore_verify.py` in the directory containing the standalone code; no third-party packages are required. These finite checks corroborate but do not replace the general algebraic proof.

## Relationship to prior work

Zaidenberg's 2006 work develops convolution equations and periodic solutions for lattice equations in prime characteristic, including reductions to semisimple and primary components. The present result specializes that general framework to the specific eight-neighbor rectangular-torus rule and supplies its exact, ground-field Jordan structure and joint transient/periodic orbit populations. Research on Moore-neighborhood linear automata with mixed boundary conditions studies another natural operator and emphasizes reversibility; those systems are not the doubly periodic torus used here. General classical algebraic methods for finite linear cellular automata are antecedents and not claimed as new. The sharp threefold-resonance split and the explicit population formulas are the contribution assessed here. A previously established four-neighbor torus classification has a related nilpotent layer but a different invertible dynamic; its full periodic-orbit conclusions do not imply the present ones.

## Limitations

The theorem requires one circumference to be a power of two and the other to be three times a power of two, both with periodic boundary conditions and with all eight Moore neighbors included. It does not classify arbitrary rectangular tori, other local kernels, odd-characteristic fields, or mixed/open boundaries. The orbit counts are exact for the defined model but are not claimed to be previously unknown in every potentially unindexed source. No independently performed audit is claimed; numerical checks only address finite dimensions.

## References

1. M. Zaidenberg, *Convolution equations on lattices: periodic solutions with values in a prime characteristic field*, arXiv:math-ph/0606070, first arXiv posting 2006-06-29, https://arxiv.org/abs/math-ph/0606070.
2. B. A. Omirov, Sh. B. Redjepov and J. B. Usmonov, *2D Moore CA with new boundary conditions and its reversibility*, arXiv:2406.06195, https://arxiv.org/abs/2406.06195.
3. O. C. Martin, A. M. Odlyzko and S. Wolfram, *Algebraic Properties of Cellular Automata*, Communications in Mathematical Physics 93 (1984), 219–258, doi:10.1007/BF01223745.
