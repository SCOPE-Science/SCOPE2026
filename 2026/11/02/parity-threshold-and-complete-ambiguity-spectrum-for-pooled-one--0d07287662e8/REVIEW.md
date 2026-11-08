# Independent mathematical audit

## correctness

PASS

Each weight-one strand with its 1 at i emits prefix/suffix length n-1 reads, so pooled labelled read-word multiplicities satisfy y_j=x_j+x_(j+1), with all-zero count fixed by k. The integer kernel is z_i=(-1)^(i-1)t. For odd n, fixed sum k forces t=0; for even n=2m fibers are integer translates with a unique representative of min odd coordinate zero. For size>=s, subtract s-1 from all m even coordinates and require at least one odd coordinate zero: T_s=B_n(k-m(s-1))-B_n(k-ms). Thus H(s)=T_s-T_(s+1), total R=B_n(k)-B_n(k-m), largest fiber 1+floor(k/m), first ambiguity at k=m one double fiber. For k growing, finite binomial difference gives R~m*k^(n-2)/(n-2)!. Independent literal-read multisets checked 42 n,k pairs (n=2..8,k=0..5) and n=4,k=4 histogram 16 singletons,8 doubles,1 triple.

## originality

PASS

Yehezkeally–Marcovich–Yaakobi study general pooled multi-strand substring read models and code-rate constructions but the inspected finite-parameter theorems do not give the weight-one n-1 read entire fiber distribution. Single-strand two-read or shorter adjacent-pair spectrum classes and prefix/suffix composition models are distinct. Exact alternating incidence-kernel rank is elementary, yet full finite fiber histogram, sharp parity threshold and code capacity are specific new observations; qualified priority.

## value

PASS

Precisely identifies when pooled longest reads lose reconstructibility and how many source multisets are confusable at every finite size, delivering exact zero-error code size and a natural parity obstruction for a standard sparse DNA-storage channel. A complete distribution, not an arbitrary small-instance computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
