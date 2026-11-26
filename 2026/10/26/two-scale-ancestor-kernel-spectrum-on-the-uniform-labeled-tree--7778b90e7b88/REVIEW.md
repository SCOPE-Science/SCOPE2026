# Independent mathematical audit

## correctness

PASS

Weighted Cayley contraction gives the stated distance probability, including the Hamiltonian path case. Conditional exchangeability gives h_n=(E L-1)/(n-2). The tree median of the three marked labels is either one of them (probability h_n for each) or another label (probability j_n for each), and the latter event at b is exactly three-component separation. Thus K=j_n I+(h_n^2-j_n)11^T, yielding both formulas. Gaussian tail domination of the rescaled distance sum gives E L/sqrt(n) -> sqrt(pi/2); hence n j_n -> 1 and the collective eigenvalue tends to pi/2-1. In particular both eigenvalues are eventually positive and the stated Euclidean condition number follows. The spectrum proof also requires noncoincidence to name the exact eigenspaces at every n: put S_k=Pr(L>=k), d=sum S_k. The survival recurrence (k+1)S_k=n(S_k-S_{k+1}) gives sum k S_k=n-d. Decreasing survival ratios give S_i S_j>=S_{i+j-1}, strictly for i=j=2. Hence d^2+d>n, and summing just the i=2 row of the nonnegative differences gives D=d^2+d-n>=1-2d/n. Now (n-2)^2[(n-3)h_n^2+3h_n-1]=(n-3)D+3d-n-1>=d(1+6/n)-4. For n>=6, x=4n/(n+6) satisfies x^2+x<=n, so d>x. At n=4,5, exact arithmetic gives h_n^2>j_n directly. I also independently enumerated connected (n-1)-edge subsets of K_n at n=4,5,6 and unioned surviving edges after deleting b: (h,j)=(5/16,1/16),(37/125,7/125),(61/216,11/216). This is a finite replay distinct from the recorded Prufer enumeration, not the all-size proof.

## originality

PASS

The kernel and its qualitative positivity are prior work, and the path law and Rayleigh mean are established inputs. The distinct finding is the exact separation/median link evaluated in this kernel and its resulting full spectrum and scale contrast. The strongest inspected antecedents do not supply these numbers: the general positivity theorem is not a spectral evaluation, and the two-vertex distance law needs a separate three-label argument to give the off-diagonal entry. No equivalent spectral statement was identified in the inspected evidence.

## value

PASS

The object is a natural complete-graph test case of the general ancestor inequality. PSD by itself predicts neither the order-one collective mode nor a vanishing transverse scale. Exact eigenvalues and the pi/2-1 coefficient distinguish these two forms of stability and give a useful quantitative benchmark without relying on small-n extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
