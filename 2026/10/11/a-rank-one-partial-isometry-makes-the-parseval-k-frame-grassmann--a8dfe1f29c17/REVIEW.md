# Independent mathematical audit

## correctness

PASS

Take \(K=2^{-1/2}\begin{pmatrix}1&0\\1&0\end{pmatrix}\), \(a=(e_1+e_2)/\sqrt2\), \(P=P_{e_1}\), the real Hadamard unitary \(U=2^{-1/2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\), \(Q=\mathrm{diag}(1,-1)\), and \(V=QU\). Direct fresh symbolic multiplication confirms \(K^*K=P\), \(K^\dagger=K^*\), \(KQ=K\), and \(KPU=KPV\), whose identical columns are \(a/\sqrt2\). The frame identity is \(\sum_j|\langle x,f_j\rangle|^2=|\langle x,a\rangle|^2=\|K^*x\|^2\) for every complex \(x\). Yet \(U^*R(K)=\operatorname{span}(e_1)\) while \(V^*R(K)=\operatorname{span}(e_2)\). The frame is literally identical, not merely equivalent. The identity \(T_F^*=U^*PK^*=U^*K^*\) proves the claimed canonical range statement, without proving a substitute bijection.

## originality

PASS

Best-of-knowledge source-specific correction. The original preprint and its published counterpart both explicitly define the line using an auxiliary unitary and claim it is well-defined. Their preceding representation theorem guarantees existence but not uniqueness of that unitary. Ordinary tight-frame Grassmannian correspondences do not settle this nonnormal rank-one operator case; available targeted searches found no stated correction, though a poorly indexed erratum remains possible.

## value

PASS

The witness invalidates the well-definedness step in a published general \(K\)-frame correspondence even with a fixed ordered Parseval frame, while identifying the invariant range that the frame does canonically determine. This is a motivated, exact correction rather than a generic frame-theory restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
